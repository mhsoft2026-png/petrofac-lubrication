
import React, { useState, useMemo, useRef } from 'react';
import { ViewState, EquipmentData, LubricantType } from './types';
import { EQUIPMENT_DATABASE } from './data';
import { askGemini } from './services/geminiService';

// --- Components ---

const Header: React.FC = () => (
  <header className="bg-gradient-to-r from-blue-900 via-blue-800 to-slate-900 px-6 py-5 sticky top-0 z-50 shadow-2xl border-b-4 border-orange-500">
    <div className="flex items-center justify-between max-w-7xl mx-auto">
      <div className="flex items-center gap-4">
        <div className="relative group">
          <div className="absolute inset-0 bg-gradient-to-br from-orange-500 to-amber-500 blur-xl opacity-60 rounded-3xl group-hover:opacity-80 transition-opacity"></div>
          <div className="relative bg-gradient-to-br from-orange-500 via-orange-600 to-amber-600 text-white p-4 rounded-3xl shadow-2xl transform group-hover:scale-105 transition-transform">
            <i className="fas fa-oil-can text-2xl"></i>
          </div>
        </div>
        <div>
          <h1 className="text-xl font-black text-white leading-none tracking-tight bg-gradient-to-r from-white to-orange-200 bg-clip-text text-transparent">LUBRIFICATION ET LUBRIFIANTS</h1>
          <p className="text-xs text-orange-300 uppercase tracking-[0.2em] font-extrabold mt-1 flex items-center gap-2">
            <span className="w-1 h-1 bg-orange-400 rounded-full"></span>
            ATL - Ain Tsila
          </p>
        </div>
      </div>
      <div className="flex items-center gap-3">
        <div className="flex items-center gap-2 bg-gradient-to-r from-emerald-500/20 to-green-500/20 px-4 py-2 rounded-full border-2 border-emerald-400/40 backdrop-blur-sm">
          <span className="relative flex h-3 w-3">
            <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
            <span className="relative inline-flex rounded-full h-3 w-3 bg-emerald-500"></span>
          </span>
          <span className="text-xs font-black text-emerald-300 uppercase tracking-wider">Système Actif</span>
        </div>
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
    <div className="px-6 py-8 bg-gradient-to-br from-slate-50 via-white to-blue-50">
      <div className="relative max-w-5xl mx-auto">
        <div className="absolute inset-0 bg-gradient-to-r from-orange-400/10 via-blue-400/10 to-purple-400/10 blur-3xl rounded-3xl"></div>
        <div className="relative space-y-4">
          <div className="flex gap-3">
            <div className="flex-1 relative group">
              <div className="absolute inset-0 bg-gradient-to-r from-orange-500 to-blue-500 rounded-2xl blur opacity-20 group-hover:opacity-30 transition-opacity"></div>
              <input 
                type="text" 
                placeholder="🔍 Rechercher: TAG, Description, Type, Marque, Grade..." 
                className="relative w-full pl-14 pr-6 py-5 bg-white/90 backdrop-blur-xl rounded-2xl text-sm text-slate-900 placeholder-slate-500 focus:outline-none focus:ring-4 focus:ring-orange-500/30 transition-all border-2 border-slate-200 focus:border-orange-500 shadow-xl font-semibold"
                onChange={(e) => onSearch(e.target.value)}
              />
              <div className="absolute left-5 top-1/2 -translate-y-1/2 text-orange-500">
                <i className="fas fa-search text-xl"></i>
              </div>
            </div>
            <button 
              onClick={() => setShowFilters(!showFilters)}
              className={`w-16 h-16 rounded-2xl flex items-center justify-center transition-all shadow-xl border-2 ${
                showFilters 
                  ? 'bg-gradient-to-br from-orange-500 to-orange-600 text-white border-orange-400 shadow-orange-500/50' 
                  : 'bg-white text-slate-700 hover:bg-slate-50 border-slate-200'
              }`}
            >
              <i className="fas fa-filter text-xl"></i>
            </button>
          </div>
          
          {showFilters && (
            <div className="bg-white/95 backdrop-blur-xl rounded-2xl p-5 border-2 border-slate-200 shadow-2xl animate-in slide-in-from-top-2 duration-200">
              <div className="flex items-center justify-between mb-4">
                <p className="text-xs font-black text-slate-600 uppercase tracking-wider flex items-center gap-2">
                  <i className="fas fa-layer-group text-orange-500"></i>
                  Filtrer par Type de Lubrifiant
                </p>
                <span className="text-xs font-bold text-slate-500 bg-slate-100 px-3 py-1 rounded-full">{resultCount} résultats</span>
              </div>
              <div className="flex gap-3 flex-wrap">
                {[
                  { type: 'الكل', label: 'Tous', icon: 'fa-th-large', color: 'slate' },
                  { type: 'OIL', label: 'Huiles', icon: 'fa-tint', color: 'blue' },
                  { type: 'GREASE', label: 'Graisses', icon: 'fa-fill-drip', color: 'emerald' }
                ].map(item => (
                  <button
                    key={item.type}
                    onClick={() => onFilterChange(item.type)}
                    className={`flex-1 px-5 py-3 rounded-xl text-sm font-black transition-all border-2 shadow-lg ${
                      filterType === item.type
                        ? `bg-gradient-to-r from-${item.color}-500 to-${item.color}-600 text-white border-${item.color}-400 shadow-${item.color}-500/50 scale-105`
                        : 'bg-slate-50 text-slate-600 border-slate-200 hover:bg-slate-100 hover:border-slate-300'
                    }`}
                  >
                    <i className={`fas ${item.icon} mr-2`}></i>
                    {item.label}
                  </button>
                ))}
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

const EquipmentCard: React.FC<{ equipment: EquipmentData; onClick: (eq: EquipmentData) => void }> = React.memo(({ equipment, onClick }) => (
  <div 
    className="group bg-gradient-to-br from-white to-slate-50 rounded-2xl p-6 border-2 border-slate-200 hover:border-orange-500 hover:shadow-2xl hover:shadow-orange-500/20 active:scale-[0.98] transition-all duration-300 cursor-pointer relative overflow-hidden"
    onClick={() => onClick(equipment)}
  >
    <div className="absolute top-0 right-0 w-40 h-40 bg-gradient-to-br from-orange-200 via-orange-100 to-transparent rounded-full -mr-20 -mt-20 opacity-30 group-hover:opacity-50 transition-opacity"></div>
    <div className="absolute bottom-0 left-0 w-32 h-32 bg-gradient-to-tr from-blue-200 via-blue-100 to-transparent rounded-full -ml-16 -mb-16 opacity-20"></div>
    
    <div className="relative">
      <div className="flex justify-between items-start mb-4">
        <div className="flex items-center gap-2">
          <div className="w-2 h-2 bg-gradient-to-r from-orange-500 to-amber-500 rounded-full animate-pulse"></div>
          <span className="text-[10px] font-black text-slate-600 bg-gradient-to-r from-slate-100 to-slate-50 px-3 py-1.5 rounded-xl uppercase tracking-wider border-2 border-slate-200">{equipment.package}</span>
        </div>
        <span className={`text-[10px] font-black px-4 py-2 rounded-xl uppercase border-2 shadow-lg ${
          equipment.type === LubricantType.OIL 
            ? 'bg-gradient-to-r from-blue-500 to-blue-600 text-white border-blue-400 shadow-blue-500/30' 
            : 'bg-gradient-to-r from-emerald-500 to-green-600 text-white border-emerald-400 shadow-emerald-500/30'
        }`}>
          <i className={`fas ${equipment.type === LubricantType.OIL ? 'fa-tint' : 'fa-fill-drip'} mr-1.5`}></i>
          {equipment.type}
        </span>
      </div>
      
      <div className="mb-4">
        <h3 className="text-2xl font-black text-slate-900 mb-2 group-hover:text-orange-600 transition-colors bg-gradient-to-r from-slate-900 to-slate-700 bg-clip-text">{equipment.tagNo}</h3>
        <p className="text-sm text-slate-600 line-clamp-2 leading-relaxed font-semibold">{equipment.description}</p>
      </div>
      
      <div className="flex items-center gap-6 text-xs font-bold border-t-2 border-slate-200 pt-4 mt-4">
        <div className="flex items-center gap-2 bg-orange-50 px-3 py-2 rounded-xl border border-orange-200">
          <i className="fas fa-flask text-orange-600"></i>
          <span className="text-slate-800">{equipment.grade}</span>
        </div>
        <div className="flex items-center gap-2 bg-blue-50 px-3 py-2 rounded-xl border border-blue-200">
          <i className="fas fa-clock text-blue-600"></i>
          <span className="text-slate-800">{equipment.replacementInterval || 'On Analysis'}</span>
        </div>
      </div>
    </div>
    
    <div className="absolute bottom-4 right-4 opacity-0 group-hover:opacity-100 transition-all duration-300 transform group-hover:translate-x-1">
      <div className="bg-orange-500 text-white p-3 rounded-xl shadow-lg">
        <i className="fas fa-arrow-right text-lg"></i>
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
    <div className="fixed inset-0 bg-white z-[60] overflow-y-auto pb-20 animate-in slide-in-from-bottom duration-300">
      <div className="sticky top-0 bg-gradient-to-r from-blue-900 to-slate-900 backdrop-blur-md p-4 border-b-2 border-orange-500 flex items-center gap-4 z-10 shadow-xl">
        <button onClick={onClose} className="p-2.5 -ml-2 text-white hover:text-orange-400 bg-white/10 rounded-xl hover:bg-white/20 transition-all">
          <i className="fas fa-arrow-left text-lg"></i>
        </button>
        <div className="flex-1">
          <h2 className="font-black text-white truncate leading-tight text-lg">{equipment.tagNo}</h2>
          <p className="text-xs text-orange-300 font-bold uppercase tracking-wide">{equipment.package}</p>
        </div>
        <div className={`px-3 py-1.5 rounded-lg font-bold text-xs ${
          equipment.type === LubricantType.OIL 
            ? 'bg-blue-500 text-white' 
            : 'bg-emerald-500 text-white'
        }`}>
          {equipment.type}
        </div>
      </div>

      <div className="p-5 space-y-6 max-w-2xl mx-auto">
        {/* Technical Data Section */}
        <section className="bg-gradient-to-br from-slate-50 to-white p-6 rounded-2xl border-2 border-slate-200 shadow-lg">
          <h4 className="text-xs uppercase font-black text-orange-600 mb-4 tracking-widest flex items-center gap-2">
            <i className="fas fa-info-circle"></i>
            Données Techniques Principales
          </h4>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div className="bg-white p-4 rounded-xl border border-slate-200">
              <p className="text-[10px] text-slate-500 mb-2 font-bold uppercase">Description</p>
              <p className="text-sm font-bold text-slate-900">{equipment.description}</p>
            </div>
            <div className="bg-white p-4 rounded-xl border border-slate-200">
              <p className="text-[10px] text-slate-500 mb-2 font-bold uppercase">Partie Spécifique</p>
              <p className="text-sm font-bold text-slate-900">{equipment.part}</p>
            </div>
          </div>
        </section>

        {/* Lubrication Parameters */}
        <section className="bg-gradient-to-br from-blue-50 to-white p-6 rounded-2xl border-2 border-blue-200 shadow-lg">
          <h4 className="text-xs uppercase font-black text-blue-700 mb-4 tracking-widest flex items-center gap-2">
            <i className="fas fa-cogs"></i>
            Paramètres de Lubrification
          </h4>
          <div className="space-y-2 bg-white border-2 border-slate-200 rounded-xl overflow-hidden shadow-md">
            {[
              { label: 'Type de Lubrifiant', val: equipment.type, icon: 'fa-tint' },
              { label: 'Grade ISO/NLGI', val: equipment.grade, icon: 'fa-vial' },
              { label: 'Volume Initial', val: equipment.initialFill, icon: 'fa-fill-drip' },
              { label: 'Intervalle de Remplissage', val: equipment.topUpInterval, icon: 'fa-hourglass-half' },
              { label: 'Durée de Vie', val: equipment.replacementInterval, icon: 'fa-redo' },
            ].map((item, idx) => (
              <div key={idx} className="flex justify-between items-center px-5 py-4 border-b last:border-0 border-slate-100 hover:bg-slate-50 transition-colors">
                <div className="flex items-center gap-3">
                  <div className="w-8 h-8 bg-gradient-to-br from-orange-500 to-orange-600 rounded-lg flex items-center justify-center">
                    <i className={`fas ${item.icon} text-white text-sm`}></i>
                  </div>
                  <span className="text-sm text-slate-700 font-bold">{item.label}</span>
                </div>
                <span className="text-sm font-black text-slate-900">{item.val}</span>
              </div>
            ))}
          </div>
        </section>

        {/* Brands Section */}
        <section className="bg-gradient-to-br from-purple-50 to-white p-6 rounded-2xl border-2 border-purple-200 shadow-lg">
          <h4 className="text-xs uppercase font-black text-purple-700 mb-4 tracking-widest flex items-center gap-2">
            <i className="fas fa-award"></i>
            Produits Équivalents par Marque
          </h4>
          <div className="grid grid-cols-1 gap-3">
            {Object.entries(equipment.brands).map(([brand, value]) => value && (
              <div key={brand} className="flex items-center gap-4 p-4 bg-white border-2 border-slate-200 rounded-xl hover:border-purple-300 hover:shadow-md transition-all">
                <div className="w-14 h-14 rounded-xl bg-gradient-to-br from-slate-100 to-slate-200 flex items-center justify-center text-xs font-black text-slate-700 uppercase border-2 border-slate-300 shadow-md">
                  {brand.slice(0, 3)}
                </div>
                <div className="flex-1">
                  <p className="text-[10px] text-slate-500 uppercase font-black tracking-wider">{brand}</p>
                  <p className="text-sm font-bold text-slate-900 mt-1">{value}</p>
                </div>
              </div>
            ))}
          </div>
        </section>

        {/* Notes Section */}
        <section className="bg-gradient-to-br from-green-50 to-white p-6 rounded-2xl border-2 border-green-300 shadow-lg">
          <div className="flex items-center justify-between mb-4">
            <h4 className="text-xs uppercase font-black text-green-700 tracking-widest flex items-center gap-2">
              <i className="fas fa-sticky-note"></i>
              Notes et Observations
            </h4>
            {!isEditing && (
              <button 
                onClick={() => setIsEditing(true)}
                className="px-4 py-2 bg-green-600 text-white rounded-xl text-xs font-bold hover:bg-green-700 transition-all shadow-md flex items-center gap-2"
              >
                <i className="fas fa-edit"></i>
                {notes ? 'Modifier' : 'Ajouter Note'}
              </button>
            )}
          </div>
          
          {isEditing ? (
            <div className="space-y-3">
              <textarea
                value={notes}
                onChange={(e) => setNotes(e.target.value)}
                placeholder="✍️ Entrez vos observations, remarques ou notes techniques..."
                className="w-full p-4 bg-white border-2 border-green-300 rounded-xl text-sm focus:outline-none focus:ring-2 focus:ring-green-500 min-h-[150px] font-medium resize-none"
              />
              <div className="flex gap-2">
                <button 
                  onClick={saveNotes}
                  className="flex-1 px-4 py-3 bg-gradient-to-r from-green-600 to-green-700 text-white rounded-xl text-sm font-black hover:from-green-700 hover:to-green-800 transition-all shadow-lg flex items-center justify-center gap-2"
                >
                  <i className="fas fa-save"></i>
                  Enregistrer
                </button>
                <button 
                  onClick={() => setIsEditing(false)}
                  className="px-4 py-3 bg-slate-200 text-slate-700 rounded-xl text-sm font-bold hover:bg-slate-300 transition-all"
                >
                  Annuler
                </button>
              </div>
            </div>
          ) : notes ? (
            <div className="bg-white p-4 rounded-xl border-2 border-slate-200 shadow-inner">
              <p className="text-sm text-slate-700 whitespace-pre-wrap font-medium leading-relaxed">{notes}</p>
            </div>
          ) : (
            <div className="text-center py-8 text-slate-400">
              <i className="fas fa-sticky-note text-5xl mb-3 opacity-30"></i>
              <p className="text-sm font-semibold">Aucune note ajoutée</p>
            </div>
          )}
        </section>

        {/* Remarks Section */}
        <section className="bg-gradient-to-br from-orange-500 to-red-600 p-6 rounded-2xl shadow-2xl text-white">
          <h4 className="text-xs uppercase font-black text-orange-100 mb-3 flex items-center gap-2">
            <i className="fas fa-exclamation-triangle"></i>
            Notes d'Ingénierie
          </h4>
          <p className="text-sm leading-relaxed font-semibold">
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
          <div className="p-6 space-y-6 bg-gradient-to-b from-slate-50 to-white min-h-screen">
            <div className="bg-gradient-to-br from-blue-900 via-blue-800 to-slate-900 rounded-3xl p-8 text-white shadow-2xl relative overflow-hidden border-4 border-orange-500/30">
              <div className="absolute top-0 right-0 w-80 h-80 bg-gradient-to-br from-orange-500/20 to-transparent rounded-full -mr-40 -mt-40"></div>
              <div className="absolute bottom-0 left-0 w-64 h-64 bg-gradient-to-tr from-blue-500/20 to-transparent rounded-full -ml-32 -mb-32"></div>
              <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full h-full">
                <div className="absolute inset-0 opacity-5">
                  <i className="fas fa-oil-can text-[20rem] text-white"></i>
                </div>
              </div>
              
              <div className="relative z-10">
                <div className="flex justify-between items-start mb-8">
                  <div>
                    <div className="flex items-center gap-2 mb-3">
                      <div className="w-1 h-8 bg-gradient-to-b from-orange-400 to-orange-600 rounded-full"></div>
                      <p className="text-xs font-black uppercase tracking-[0.25em] text-orange-300">Système de Lubrification</p>
                    </div>
                    <h2 className="text-4xl font-black leading-tight bg-gradient-to-r from-white via-orange-100 to-white bg-clip-text text-transparent">BASE DE DONNÉES<br/>LUBRIFIANTS ATL</h2>
                    <p className="text-sm text-blue-200 mt-2 font-bold">Ain Tsila Production Facility</p>
                  </div>
                  <div className="relative">
                    <div className="absolute inset-0 bg-gradient-to-br from-orange-500 to-amber-600 blur-xl opacity-50"></div>
                    <div className="relative w-20 h-20 bg-gradient-to-br from-orange-500 via-orange-600 to-amber-600 backdrop-blur-xl rounded-3xl flex items-center justify-center border-2 border-orange-400/50 shadow-2xl transform hover:scale-110 transition-transform">
                      <i className="fas fa-database text-3xl"></i>
                    </div>
                  </div>
                </div>
                
                <div className="grid grid-cols-2 gap-4">
                  <div className="bg-gradient-to-br from-white/10 to-white/5 backdrop-blur-xl p-6 rounded-2xl border-2 border-white/20 shadow-xl hover:border-orange-400/50 transition-all group">
                    <div className="flex items-center gap-3 mb-3">
                      <div className="w-10 h-10 bg-orange-500/20 rounded-xl flex items-center justify-center border border-orange-400/30">
                        <i className="fas fa-cogs text-orange-400"></i>
                      </div>
                      <p className="text-xs text-white/80 font-black uppercase tracking-wide">Total Équipements</p>
                    </div>
                    <p className="text-5xl font-black bg-gradient-to-r from-white to-orange-200 bg-clip-text text-transparent">{EQUIPMENT_DATABASE.length}</p>
                    <p className="text-xs text-blue-300 mt-2 font-bold">Machines actives</p>
                  </div>
                  
                  <div className="bg-gradient-to-br from-white/10 to-white/5 backdrop-blur-xl p-6 rounded-2xl border-2 border-white/20 shadow-xl hover:border-emerald-400/50 transition-all group">
                    <div className="flex items-center gap-3 mb-3">
                      <div className="w-10 h-10 bg-emerald-500/20 rounded-xl flex items-center justify-center border border-emerald-400/30">
                        <i className="fas fa-check-circle text-emerald-400"></i>
                      </div>
                      <p className="text-xs text-white/80 font-black uppercase tracking-wide">État Système</p>
                    </div>
                    <div className="flex items-center gap-3 mb-2">
                      <span className="relative flex h-4 w-4">
                        <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                        <span className="relative inline-flex rounded-full h-4 w-4 bg-emerald-500"></span>
                      </span>
                      <p className="text-2xl font-black text-emerald-300">OPÉRATIONNEL</p>
                    </div>
                    <p className="text-xs text-blue-300 font-bold">Synchronisé en temps réel</p>
                  </div>
                </div>
              </div>
            </div>

            <section className="relative">
              <div className="flex items-center justify-between mb-6 px-1">
                <div>
                  <h3 className="text-2xl font-black text-slate-900 uppercase tracking-tight flex items-center gap-3">
                    <div className="w-2 h-10 bg-gradient-to-b from-orange-500 to-orange-600 rounded-full"></div>
                    Équipements Récents
                  </h3>
                  <p className="text-sm text-slate-500 font-semibold mt-2 ml-5">Dernières entrées dans la base de données</p>
                </div>
                <button onClick={() => setCurrentView('search')} className="group flex items-center gap-2 text-sm font-black text-white bg-gradient-to-r from-orange-500 to-orange-600 px-6 py-3.5 rounded-xl uppercase tracking-wide hover:from-orange-600 hover:to-orange-700 transition-all border-2 border-orange-400 shadow-xl shadow-orange-500/30 hover:shadow-2xl hover:shadow-orange-500/50">
                  Voir Tout
                  <i className="fas fa-arrow-left group-hover:translate-x-1 transition-transform"></i>
                </button>
              </div>
              <div className="space-y-5">
                {EQUIPMENT_DATABASE.slice(0, 6).map(eq => (
                  <EquipmentCard key={eq.id} equipment={eq} onClick={setSelectedEquipment} />
                ))}
              </div>
            </section>
          </div>
        );
      case 'search':
        return (
          <div className="flex flex-col h-full overflow-hidden bg-gradient-to-b from-slate-50 to-white">
            <SearchBar 
              onSearch={setSearchTerm} 
              filterType={filterType}
              onFilterChange={setFilterType}
              resultCount={filteredEquipment.length}
            />
            <div className="flex-1 overflow-y-auto p-6">
              <div className="flex justify-between items-center mb-6 sticky top-0 bg-white/80 backdrop-blur-xl z-10 pb-4 rounded-2xl">
                <div>
                  <h2 className="text-2xl font-black text-slate-900">قائمة المعدات</h2>
                  <p className="text-sm text-slate-500 mt-1 font-semibold">
                    {filteredEquipment.length === 0 ? 'لا توجد نتائج' : 
                     filteredEquipment.length === 1 ? 'نتيجة واحدة' : 
                     `${filteredEquipment.length} نتيجة`}
                    {searchTerm && ` - البحث عن: "${searchTerm}"`}
                  </p>
                </div>
              </div>
              <div className="space-y-4">
                {displayedEquipment.map(eq => (
                  <EquipmentCard key={eq.id} equipment={eq} onClick={setSelectedEquipment} />
                ))}
              </div>
              {displayedEquipment.length < filteredEquipment.length && (
                <div className="text-center py-8">
                  <button 
                    onClick={() => setDisplayLimit(prev => prev + 50)}
                    className="px-8 py-4 bg-gradient-to-r from-orange-500 to-orange-600 text-white rounded-2xl font-black text-sm shadow-2xl hover:shadow-orange-500/50 hover:scale-105 transition-all border border-orange-400"
                  >
                    <i className="fas fa-chevron-down mr-2"></i>
                    تحميل المزيد ({filteredEquipment.length - displayedEquipment.length} متبقية)
                  </button>
                </div>
              )}
              {filteredEquipment.length === 0 && (
                <div className="text-center py-32 px-12">
                  <div className="w-24 h-24 bg-orange-50 rounded-3xl flex items-center justify-center mx-auto mb-6 border-2 border-orange-200">
                    <i className="fas fa-search-minus text-5xl text-orange-400"></i>
                  </div>
                  <h3 className="text-xl font-black text-slate-900 mb-3">لم يتم العثور على نتائج</h3>
                  <p className="text-sm text-slate-500 leading-relaxed max-w-md mx-auto">
                    لم نجد أي معدات تطابق بحثك. جرب استخدام أرقام المعدات أو الأوصاف.
                  </p>
                  <button 
                    onClick={() => { setSearchTerm(''); setFilterType('الكل'); }}
                    className="mt-6 px-6 py-3 bg-orange-500 text-white rounded-xl font-bold hover:bg-orange-600 transition-all"
                  >
                    مسح البحث
                  </button>
                </div>
              )}
            </div>
          </div>
        );
      case 'ai':
        return <AIExpert />;
      default:
        return null;
    }
  };

  return (
    <div className="flex flex-col h-screen max-w-7xl mx-auto bg-white overflow-hidden font-sans">
      <Header />
      
      <main className="flex-1 overflow-y-auto relative pb-24 scroll-smooth">
        {renderContent()}
      </main>

      {selectedEquipment && (
        <DetailView 
          equipment={selectedEquipment} 
          onClose={() => setSelectedEquipment(null)} 
        />
      )}

      <nav className="fixed bottom-0 left-0 right-0 bg-white/95 backdrop-blur-2xl border-t-2 border-slate-200 py-4 px-6 z-40 max-w-7xl mx-auto shadow-2xl">
        <div className="flex justify-around items-center relative">
          {[
            { id: 'dashboard', icon: 'fa-home', label: 'الرئيسية' },
            { id: 'search', icon: 'fa-search', label: 'البحث' },
            { id: 'ai', icon: 'fa-robot', label: 'مساعد AI' }
          ].map((item) => (
            <button 
              key={item.id}
              onClick={() => setCurrentView(item.id as ViewState)}
              className={`flex flex-col items-center gap-1.5 transition-all duration-300 relative group flex-1 ${
                currentView === item.id ? 'scale-110' : ''
              }`}
            >
              <div className={`w-14 h-14 rounded-2xl flex items-center justify-center transition-all shadow-lg ${
                currentView === item.id 
                  ? 'bg-gradient-to-br from-orange-500 to-orange-600 shadow-orange-500/50' 
                  : 'bg-slate-100 group-hover:bg-slate-200'
              }`}>
                <i className={`fas ${item.icon} text-xl ${currentView === item.id ? 'text-white' : 'text-slate-600'}`}></i>
              </div>
              <span className={`text-[10px] font-bold ${
                currentView === item.id ? 'text-orange-600' : 'text-slate-500'
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
