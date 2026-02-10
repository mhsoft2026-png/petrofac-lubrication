
import React, { useState, useMemo, useRef } from 'react';
import { ViewState, EquipmentData, LubricantType } from './types';
import { EQUIPMENT_DATABASE } from './data';
import { askGemini } from './services/geminiService';

// --- Components ---

const Header: React.FC = () => (
  <header className="bg-white border-b-2 border-slate-200 px-6 py-4 sticky top-0 z-50 shadow-md backdrop-blur-lg bg-white/95">
    <div className="flex items-center justify-between max-w-7xl mx-auto">
      <div className="flex items-center gap-3">
        <div className="bg-gradient-to-br from-blue-600 to-blue-700 text-white p-3 rounded-xl shadow-lg">
          <i className="fas fa-oil-can text-xl"></i>
        </div>
        <div>
          <h1 className="text-lg font-bold text-slate-800 leading-tight">LUBRIFICATION ET LUBRIFIANTS</h1>
          <p className="text-xs text-slate-500 font-medium mt-0.5">ATL - Ain Tsila</p>
        </div>
      </div>
      <div className="flex items-center gap-2 bg-emerald-50 px-3 py-1.5 rounded-lg border border-emerald-200">
        <span className="w-2 h-2 bg-emerald-500 rounded-full animate-pulse"></span>
        <span className="text-xs font-semibold text-emerald-700">Actif</span>
      </div>
    </div>
  </header>
);

const SearchBar: React.FC<{ 
  onSearch: (val: string) => void; 
  filterType: string;
  onFilterChange: (type: string) => void;
  resultCount: number;
}> = ({ onSearch, filterType, onFilterChange, resultCount }) => {
  const [showFilters, setShowFilters] = React.useState(false);
  
  return (
    <div className="px-6 py-6 bg-slate-50">
      <div className="max-w-5xl mx-auto space-y-4">
        <div className="flex gap-3">
          <div className="flex-1 relative">
            <input 
              type="text" 
              placeholder="🔍 Rechercher par TAG, Description, Type, Marque..." 
              className="w-full pl-12 pr-4 py-3.5 bg-white rounded-xl text-sm text-slate-800 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all border border-slate-200 shadow-sm"
              onChange={(e) => onSearch(e.target.value)}
            />
            <div className="absolute left-4 top-1/2 -translate-y-1/2 text-slate-400">
              <i className="fas fa-search"></i>
            </div>
          </div>
          <button 
            onClick={() => setShowFilters(!showFilters)}
            className={`px-4 py-3.5 rounded-xl flex items-center gap-2 transition-all border font-semibold text-sm ${
              showFilters 
                ? 'bg-blue-600 text-white border-blue-600 shadow-md' 
                : 'bg-white text-slate-700 hover:bg-slate-50 border-slate-200 shadow-sm'
            }`}
          >
            <i className="fas fa-filter"></i>
            <span className="hidden sm:inline">Filtres</span>
          </button>
        </div>
        
        {showFilters && (
          <div className="bg-white rounded-xl p-4 border border-slate-200 shadow-sm animate-in slide-in-from-top-2 duration-200">
            <div className="flex items-center justify-between mb-3">
              <p className="text-xs font-semibold text-slate-600 uppercase tracking-wide">
                Type de Lubrifiant
              </p>
              <span className="text-xs font-medium text-slate-500 bg-slate-100 px-2.5 py-1 rounded-full">{resultCount} résultats</span>
            </div>
            <div className="flex gap-2 flex-wrap">
              {[
                { type: 'الكل', label: 'Tous', icon: 'fa-th-large' },
                { type: 'OIL', label: 'Huiles', icon: 'fa-tint' },
                { type: 'GREASE', label: 'Graisses', icon: 'fa-fill-drip' }
              ].map(item => (
                <button
                  key={item.type}
                  onClick={() => onFilterChange(item.type)}
                  className={`flex-1 px-4 py-2.5 rounded-lg text-sm font-semibold transition-all border ${
                    filterType === item.type
                      ? 'bg-blue-600 text-white border-blue-600 shadow-md'
                      : 'bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100'
                  }`}
                >
                  <i className={`fas ${item.icon} mr-1.5`}></i>
                  {item.label}
                </button>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

const EquipmentCard: React.FC<{ equipment: EquipmentData; onClick: (eq: EquipmentData) => void }> = React.memo(({ equipment, onClick }) => (
  <div 
    className="bg-white rounded-xl p-5 border border-slate-200 hover:border-blue-400 hover:shadow-lg active:scale-[0.99] transition-all cursor-pointer"
    onClick={() => onClick(equipment)}
  >
    <div className="flex justify-between items-start mb-3">
      <span className="text-xs font-medium text-slate-500 bg-slate-50 px-2.5 py-1 rounded-lg">{equipment.package}</span>
      <span className={`text-xs font-semibold px-3 py-1 rounded-lg ${
        equipment.type === LubricantType.OIL 
          ? 'bg-blue-100 text-blue-700' 
          : 'bg-emerald-100 text-emerald-700'
      }`}>
        <i className={`fas ${equipment.type === LubricantType.OIL ? 'fa-tint' : 'fa-fill-drip'} mr-1`}></i>
        {equipment.type}
      </span>
    </div>
    
    <h3 className="text-xl font-bold text-slate-800 mb-2">{equipment.tagNo}</h3>
    <p className="text-sm text-slate-600 line-clamp-2 mb-4">{equipment.description}</p>
    
    <div className="flex items-center gap-3 text-xs">
      <div className="flex items-center gap-1.5 text-slate-600">
        <i className="fas fa-flask text-blue-500"></i>
        <span className="font-medium">{equipment.grade}</span>
      </div>
      <div className="flex items-center gap-1.5 text-slate-600">
        <i className="fas fa-clock text-emerald-500"></i>
        <span className="font-medium">{equipment.replacementInterval || 'Sur Analyse'}</span>
      </div>
    </div>
  </div>
));

const DetailView: React.FC<{ equipment: EquipmentData; onClose: () => void }> = ({ equipment, onClose }) => {
  const [notes, setNotes] = React.useState<string>('');
  const [isEditing, setIsEditing] = React.useState(false);
  
  React.useEffect(() => {
    const savedNotes = localStorage.getItem(`equipment-note-${equipment.id}`);
    if (savedNotes) {
      setNotes(savedNotes);
    }
  }, [equipment.id]);
  
  const saveNotes = () => {
    localStorage.setItem(`equipment-note-${equipment.id}`, notes);
    setIsEditing(false);
  };
  
  return (
    <div className="fixed inset-0 bg-slate-50 z-[60] overflow-y-auto pb-20 animate-in slide-in-from-right duration-200">
      <div className="sticky top-0 bg-white border-b border-slate-200 p-4 flex items-center gap-3 z-10 shadow-sm">
        <button onClick={onClose} className="p-2 -ml-1 text-slate-600 hover:text-blue-600 hover:bg-slate-100 rounded-lg transition-all">
          <i className="fas fa-arrow-left"></i>
        </button>
        <div className="flex-1">
          <h2 className="font-bold text-slate-800 truncate">{equipment.tagNo}</h2>
          <p className="text-xs text-slate-500">{equipment.package}</p>
        </div>
        <div className={`px-3 py-1 rounded-lg font-medium text-xs ${
          equipment.type === LubricantType.OIL 
            ? 'bg-blue-100 text-blue-700' 
            : 'bg-emerald-100 text-emerald-700'
        }`}>
          {equipment.type}
        </div>
      </div>

      <div className="p-4 space-y-4 max-w-2xl mx-auto">
        {/* Technical Data Section */}
        <section className="bg-white p-4 rounded-xl border border-slate-200">
          <h4 className="text-xs font-semibold text-slate-600 mb-3 flex items-center gap-2">
            <i className="fas fa-info-circle text-blue-500"></i>
            Données Techniques
          </h4>
          <div className="space-y-3">
            <div>
              <p className="text-xs text-slate-500 mb-1">Description</p>
              <p className="text-sm font-medium text-slate-800">{equipment.description}</p>
            </div>
            <div>
              <p className="text-xs text-slate-500 mb-1">Partie Spécifique</p>
              <p className="text-sm font-medium text-slate-800">{equipment.part}</p>
            </div>
          </div>
        </section>

        {/* Lubrication Parameters */}
        <section className="bg-white p-4 rounded-xl border border-slate-200">
          <h4 className="text-xs font-semibold text-slate-600 mb-3 flex items-center gap-2">
            <i className="fas fa-cogs text-blue-500"></i>
            Paramètres de Lubrification
          </h4>
          <div className="space-y-2">
            {[
              { label: 'Type', val: equipment.type },
              { label: 'Grade ISO/NLGI', val: equipment.grade },
              { label: 'Volume Initial', val: equipment.initialFill },
              { label: 'Intervalle Remplissage', val: equipment.topUpInterval },
              { label: 'Durée de Vie', val: equipment.replacementInterval },
            ].map((item, idx) => (
              <div key={idx} className="flex justify-between items-center py-2 border-b last:border-0 border-slate-100">
                <span className="text-xs text-slate-600">{item.label}</span>
                <span className="text-sm font-medium text-slate-800">{item.val}</span>
              </div>
            ))}
          </div>
        </section>

        {/* Brands Section */}
        <section className="bg-white p-4 rounded-xl border border-slate-200">
          <h4 className="text-xs font-semibold text-slate-600 mb-3 flex items-center gap-2">
            <i className="fas fa-award text-blue-500"></i>
            Produits par Marque
          </h4>
          <div className="space-y-2">
            {Object.entries(equipment.brands).map(([brand, value]) => value && (
              <div key={brand} className="flex items-center justify-between py-2 border-b last:border-0 border-slate-100">
                <span className="text-xs font-medium text-slate-600">{brand}</span>
                <span className="text-sm font-medium text-slate-800">{value}</span>
              </div>
            ))}
          </div>
        </section>

        {/* Notes Section */}
        <section className="bg-white p-4 rounded-xl border border-slate-200">
          <div className="flex items-center justify-between mb-3">
            <h4 className="text-xs font-semibold text-slate-600 flex items-center gap-2">
              <i className="fas fa-sticky-note text-blue-500"></i>
              Notes
            </h4>
            {!isEditing && (
              <button 
                onClick={() => setIsEditing(true)}
                className="px-3 py-1.5 bg-blue-600 text-white rounded-lg text-xs font-medium hover:bg-blue-700 transition-all flex items-center gap-1.5"
              >
                <i className="fas fa-edit"></i>
                {notes ? 'Modifier' : 'Ajouter'}
              </button>
            )}
          </div>
          
          {isEditing ? (
            <div className="space-y-2">
              <textarea
                value={notes}
                onChange={(e) => setNotes(e.target.value)}
                placeholder="اكتب ملاحظاتك هنا... يمكنك كتابة معلومات تقنية، ملاحظات الصيانة، أو أي معلومات مفيدة."
                className="w-full p-4 bg-white border-2 border-blue-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 min-h-[180px] resize-y"
                autoFocus
              />
              <div className="flex gap-2">
                <button 
                  onClick={saveNotes}
                  className="flex-1 px-3 py-2 bg-blue-600 text-white rounded-lg text-sm font-medium hover:bg-blue-700 transition-all"
                >
                  Enregistrer
                </button>
                <button 
                  onClick={() => setIsEditing(false)}
                  className="px-3 py-2 bg-slate-100 text-slate-600 rounded-lg text-sm font-medium hover:bg-slate-200 transition-all"
                >
                  Annuler
                </button>
              </div>
            </div>
          ) : notes ? (
            <div className="bg-slate-50 p-3 rounded-lg border border-slate-200">
              <p className="text-sm text-slate-700 whitespace-pre-wrap leading-relaxed">{notes}</p>
            </div>
          ) : (
            <div className="text-center py-6 text-slate-400">
              <i className="fas fa-sticky-note text-3xl mb-2 opacity-30"></i>
              <p className="text-xs">Aucune note</p>
            </div>
          )}
        </section>

        {/* Remarks Section */}
        <section className="bg-amber-50 p-4 rounded-xl border border-amber-200">
          <h4 className="text-xs font-semibold text-amber-700 mb-2 flex items-center gap-2">
            <i className="fas fa-exclamation-triangle"></i>
            Notes d'Ingénierie
          </h4>
          <p className="text-sm text-amber-900 leading-relaxed">
            {equipment.remarks}
          </p>
        </section>
      </div>
    </div>
  );
};

const AIExpert: React.FC = () => {
  const [query, setQuery] = useState('');
  const [selectedImage, setSelectedImage] = useState<string | null>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);
  const [messages, setMessages] = useState<{role: 'user' | 'bot', text: string, image?: string}[]>([
    {role: 'bot', text: "Département Ingénierie mis à jour. La base de données principale d'Ain Tsila est maintenant entièrement intégrée. Posez-moi des questions sur n'importe quel système (séries 100, 301, 401, 800) ou scannez une page de manuel technique."}
  ]);
  const [loading, setLoading] = useState(false);

  const handleImageSelect = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      const reader = new FileReader();
      reader.onloadend = () => setSelectedImage(reader.result as string);
      reader.readAsDataURL(file);
    }
  };

  const handleAsk = async () => {
    if (!query.trim() && !selectedImage) return;
    const userMsg = query;
    const userImg = selectedImage;
    setMessages(prev => [...prev, { role: 'user', text: userMsg || "Analyse en cours...", image: userImg || undefined }]);
    setQuery('');
    setSelectedImage(null);
    setLoading(true);
    const botResponse = await askGemini(userMsg, userImg?.split(',')[1]);
    setMessages(prev => [...prev, { role: 'bot', text: botResponse || 'Erreur système. Veuillez réessayer.' }]);
    setLoading(false);
  };

  return (
    <div className="h-full flex flex-col bg-slate-50">
      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {messages.map((m, i) => (
          <div key={i} className={`flex ${m.role === 'user' ? 'justify-end' : 'justify-start'}`}>
            <div className={`max-w-[85%] p-4 rounded-2xl text-sm ${
              m.role === 'user' ? 'bg-orange-600 text-white rounded-tr-none' : 'bg-white text-slate-800 shadow-sm border border-slate-100 rounded-tl-none'
            }`}>
              {m.image && <img src={m.image} alt="Upload" className="w-full rounded-lg mb-2 border border-white/20" />}
              {m.text}
            </div>
          </div>
        ))}
        {loading && (
          <div className="flex justify-start">
            <div className="bg-white p-3 rounded-2xl shadow-sm border border-slate-100 flex gap-1">
              <div className="w-1.5 h-1.5 bg-slate-400 rounded-full animate-bounce"></div>
              <div className="w-1.5 h-1.5 bg-slate-400 rounded-full animate-bounce delay-100"></div>
              <div className="w-1.5 h-1.5 bg-slate-400 rounded-full animate-bounce delay-200"></div>
            </div>
          </div>
        )}
      </div>
      <div className="p-4 bg-white border-t border-slate-100">
        {selectedImage && (
          <div className="mb-2 p-2 bg-orange-50 rounded-xl flex items-center justify-between border border-orange-100">
            <div className="flex items-center gap-2">
              <img src={selectedImage} className="w-12 h-12 object-cover rounded border" alt="Preview" />
              <span className="text-[10px] font-bold text-orange-600">Scan Manuel Prêt</span>
            </div>
            <button onClick={() => setSelectedImage(null)} className="text-slate-400"><i className="fas fa-times"></i></button>
          </div>
        )}
        <div className="flex items-center gap-2">
          <button onClick={() => fileInputRef.current?.click()} className="w-12 h-12 bg-slate-100 text-slate-500 rounded-xl flex items-center justify-center hover:bg-slate-200 transition-colors">
            <i className="fas fa-camera text-lg"></i>
          </button>
          <input type="file" ref={fileInputRef} className="hidden" accept="image/*" onChange={handleImageSelect} />
          <input 
            type="text" value={query} onChange={(e) => setQuery(e.target.value)} onKeyPress={(e) => e.key === 'Enter' && handleAsk()}
            placeholder="Rechercher des tags ou demander à l'IA..." className="flex-1 px-4 py-3 bg-slate-100 rounded-xl text-sm focus:outline-none focus:ring-2 focus:ring-orange-600"
          />
          <button onClick={handleAsk} disabled={loading || (!query.trim() && !selectedImage)} className="w-12 h-12 bg-orange-600 text-white rounded-xl flex items-center justify-center disabled:opacity-50 shadow-lg shadow-orange-200">
            <i className="fas fa-paper-plane"></i>
          </button>
        </div>
      </div>
    </div>
  );
};

// --- Main App ---

export default function App() {
  const [currentView, setCurrentView] = useState<ViewState>('dashboard');
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedEquipment, setSelectedEquipment] = useState<EquipmentData | null>(null);
  const [displayLimit, setDisplayLimit] = useState(50);
  const [filterType, setFilterType] = useState('الكل');

  // Get equipment with notes from localStorage
  const getModifiedEquipment = useMemo(() => {
    const equipmentWithNotes: EquipmentData[] = [];
    EQUIPMENT_DATABASE.forEach(equipment => {
      const savedNote = localStorage.getItem(`equipment-note-${equipment.id}`);
      if (savedNote && savedNote.trim()) {
        equipmentWithNotes.push(equipment);
      }
    });
    return equipmentWithNotes;
  }, [currentView]); // Re-calculate when view changes to refresh list

  const filteredEquipment = useMemo(() => {
    const term = searchTerm.toLowerCase().trim();
    let results = EQUIPMENT_DATABASE;
    
    // Apply type filter first
    if (filterType !== 'الكل') {
      results = results.filter(item => item.type === filterType);
    }
    
    // If no search term, return filtered results
    if (!term) return results;
    
    // Enhanced search logic
    return results.filter(item => {
      // Search in Tag Number
      if (item.tagNo.toLowerCase().includes(term)) return true;
      
      // Search in Description
      if (item.description.toLowerCase().includes(term)) return true;
      
      // Search in Package
      if (item.package.toLowerCase().includes(term)) return true;
      
      // Search in Part
      if (item.part.toLowerCase().includes(term)) return true;
      
      // Search in Grade
      if (item.grade.toLowerCase().includes(term)) return true;
      
      // Search in Type
      if (item.type.toLowerCase().includes(term)) return true;
      
      // Search in Brands
      const brandValues = Object.values(item.brands).filter(v => v);
      if (brandValues.some(brand => brand.toLowerCase().includes(term))) return true;
      
      // Search in Initial Fill
      if (item.initialFill.toLowerCase().includes(term)) return true;
      
      // Search in Intervals
      if (item.topUpInterval?.toLowerCase().includes(term)) return true;
      if (item.replacementInterval?.toLowerCase().includes(term)) return true;
      
      return false;
    });
  }, [searchTerm, filterType]);

  const displayedEquipment = useMemo(() => {
    return filteredEquipment
      .sort((a, b) => a.tagNo.localeCompare(b.tagNo, undefined, { numeric: true }))
      .slice(0, displayLimit);
  }, [filteredEquipment, displayLimit]);

  const renderContent = () => {
    switch (currentView) {
      case 'dashboard':
        return (
          <div className="p-6 space-y-6 bg-slate-50 min-h-screen">
            <div className="bg-gradient-to-br from-blue-600 to-blue-700 rounded-2xl p-6 text-white shadow-lg">
              <div className="flex justify-between items-start mb-6">
                <div>
                  <p className="text-xs font-medium text-blue-200 mb-1">Système de Lubrification</p>
                  <h2 className="text-2xl font-bold mb-1">Base de Données ATL</h2>
                  <p className="text-xs text-blue-200">Ain Tsila Production Facility</p>
                </div>
                <div className="w-12 h-12 bg-white/20 backdrop-blur rounded-xl flex items-center justify-center">
                  <i className="fas fa-database text-xl"></i>
                </div>
              </div>
              
              <div className="grid grid-cols-2 gap-3">
                <div className="bg-white/10 backdrop-blur p-4 rounded-xl border border-white/20">
                  <div className="flex items-center gap-2 mb-2">
                    <i className="fas fa-cogs text-sm"></i>
                    <p className="text-xs font-medium">Total</p>
                  </div>
                  <p className="text-3xl font-bold">{EQUIPMENT_DATABASE.length}</p>
                  <p className="text-xs text-blue-200 mt-1">Équipements</p>
                </div>
                
                <div className="bg-white/10 backdrop-blur p-4 rounded-xl border border-white/20">
                  <div className="flex items-center gap-2 mb-2">
                    <span className="w-2 h-2 bg-emerald-400 rounded-full animate-pulse"></span>
                    <p className="text-xs font-medium">État</p>
                  </div>
                  <p className="text-lg font-bold text-emerald-300">Actif</p>
                  <p className="text-xs text-blue-200 mt-1">Temps réel</p>
                </div>
              </div>
            </div>

            <section>
              <div className="flex items-center justify-between mb-4">
                <div>
                  <h3 className="text-lg font-bold text-slate-800">Équipements Récents</h3>
                  <p className="text-xs text-slate-500 mt-0.5">Dernières entrées</p>
                </div>
                <button onClick={() => setCurrentView('search')} className="flex items-center gap-2 text-sm font-semibold text-blue-600 hover:text-blue-700 bg-blue-50 px-4 py-2 rounded-lg hover:bg-blue-100 transition-all">
                  Voir Tout
                  <i className="fas fa-arrow-left text-xs"></i>
                </button>
              </div>
              <div className="space-y-3">{EQUIPMENT_DATABASE.slice(0, 6).map(eq => (
                  <EquipmentCard key={eq.id} equipment={eq} onClick={setSelectedEquipment} />
                ))}
              </div>
            </section>
          </div>
        );
      case 'search':
        return (
          <div className="flex flex-col h-full overflow-hidden bg-slate-50">
            <SearchBar 
              onSearch={setSearchTerm} 
              filterType={filterType}
              onFilterChange={setFilterType}
              resultCount={filteredEquipment.length}
            />
            <div className="flex-1 overflow-y-auto p-6">
              <div className="flex justify-between items-center mb-4">
                <div>
                  <h2 className="text-lg font-bold text-slate-800">قائمة المعدات</h2>
                  <p className="text-xs text-slate-500 mt-0.5">
                    {filteredEquipment.length === 0 ? 'لا توجد نتائج' : 
                     filteredEquipment.length === 1 ? 'نتيجة واحدة' : 
                     `${filteredEquipment.length} نتيجة`}
                    {searchTerm && ` - البحث عن: "${searchTerm}"`}
                  </p>
                </div>
              </div>
              <div className="space-y-3">
                {displayedEquipment.map(eq => (
                  <EquipmentCard key={eq.id} equipment={eq} onClick={setSelectedEquipment} />
                ))}
              </div>
              {displayedEquipment.length < filteredEquipment.length && (
                <div className="text-center py-6">
                  <button 
                    onClick={() => setDisplayLimit(prev => prev + 50)}
                    className="px-6 py-3 bg-blue-600 text-white rounded-xl font-semibold text-sm hover:bg-blue-700 transition-all"
                  >
                    <i className="fas fa-chevron-down mr-2"></i>
                    تحميل المزيد ({filteredEquipment.length - displayedEquipment.length} متبقية)
                  </button>
                </div>
              )}
              {filteredEquipment.length === 0 && (
                <div className="text-center py-20 px-8">
                  <div className="w-20 h-20 bg-slate-100 rounded-2xl flex items-center justify-center mx-auto mb-4">
                    <i className="fas fa-search-minus text-4xl text-slate-400"></i>
                  </div>
                  <h3 className="text-lg font-bold text-slate-800 mb-2">لم يتم العثور على نتائج</h3>
                  <p className="text-sm text-slate-500 max-w-md mx-auto mb-4">
                    لم نجد أي معدات تطابق بحثك. جرب استخدام أرقام المعدات أو الأوصاف.
                  </p>
                  <button 
                    onClick={() => { setSearchTerm(''); setFilterType('الكل'); }}
                    className="px-5 py-2.5 bg-blue-600 text-white rounded-lg font-medium hover:bg-blue-700 transition-all"
                  >
                    مسح البحث
                  </button>
                </div>
              )}
            </div>
          </div>
        );
      case 'modified':
        return (
          <div className="p-6 space-y-4 bg-slate-50 min-h-screen">
            <div className="mb-6">
              <h2 className="text-lg font-bold text-slate-800">المعدات المعدلة</h2>
              <p className="text-xs text-slate-500 mt-0.5">
                {getModifiedEquipment.length === 0 
                  ? 'لا توجد معدات معدلة' 
                  : `${getModifiedEquipment.length} معدات تحتوي على ملاحظات`}
              </p>
            </div>
            
            {getModifiedEquipment.length > 0 ? (
              <div className="space-y-3">
                {getModifiedEquipment.map(eq => (
                  <EquipmentCard key={eq.id} equipment={eq} onClick={setSelectedEquipment} />
                ))}
              </div>
            ) : (
              <div className="text-center py-20 px-8">
                <div className="w-20 h-20 bg-slate-100 rounded-2xl flex items-center justify-center mx-auto mb-4">
                  <i className="fas fa-sticky-note text-4xl text-slate-400"></i>
                </div>
                <h3 className="text-lg font-bold text-slate-800 mb-2">لا توجد معدات معدلة</h3>
                <p className="text-sm text-slate-500 max-w-md mx-auto mb-4">
                  لم تقم بإضافة ملاحظات لأي معدة بعد. ابدأ بالبحث عن المعدات وإضافة ملاحظاتك.
                </p>
                <button 
                  onClick={() => setCurrentView('search')}
                  className="px-5 py-2.5 bg-blue-600 text-white rounded-lg font-medium hover:bg-blue-700 transition-all inline-flex items-center gap-2"
                >
                  <i className="fas fa-search"></i>
                  ابحث عن معدة
                </button>
              </div>
            )}
          </div>
        );
      case 'ai':
        return <AIExpert />;
      default:
        return null;
    }
  };

  return (
    <div className="flex flex-col h-screen max-w-7xl mx-auto bg-slate-50 overflow-hidden font-sans">
      <Header />
      
      <main className="flex-1 overflow-y-auto relative pb-20 scroll-smooth">
        {renderContent()}
      </main>

      {selectedEquipment && (
        <DetailView 
          equipment={selectedEquipment} 
          onClose={() => setSelectedEquipment(null)} 
        />
      )}

      <nav className="fixed bottom-0 left-0 right-0 bg-white border-t border-slate-200 py-2 px-2 z-40 max-w-7xl mx-auto shadow-lg">
        <div className="flex justify-around items-center">
          {[
            { id: 'dashboard', icon: 'fa-home', label: 'الرئيسية' },
            { id: 'search', icon: 'fa-search', label: 'البحث' },
            { id: 'modified', icon: 'fa-edit', label: 'المعدلة' },
            { id: 'ai', icon: 'fa-robot', label: 'AI' }
          ].map((item) => (
            <button 
              key={item.id}
              onClick={() => setCurrentView(item.id as ViewState)}
              className={`flex flex-col items-center gap-1 transition-all flex-1 py-2 rounded-lg ${
                currentView === item.id ? 'bg-blue-50' : ''
              }`}
            >
              <div className={`w-10 h-10 rounded-xl flex items-center justify-center transition-all ${
                currentView === item.id 
                  ? 'bg-blue-600 text-white' 
                  : 'text-slate-500'
              }`}>
                <i className={`fas ${item.icon}`}></i>
              </div>
              <span className={`text-[10px] font-medium ${
                currentView === item.id ? 'text-blue-600' : 'text-slate-500'
              }`}>
                {item.label}
              </span>
            </button>
          ))}
        </div>
      </nav>
    </div>
  );
}
