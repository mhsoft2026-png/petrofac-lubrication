
import React, { useState, useMemo, useRef } from 'react';
import { ViewState, EquipmentData, LubricantType } from './types';
import { EQUIPMENT_DATABASE } from './data';
import { askGemini } from './services/geminiService';

// --- Components ---

const Header: React.FC = () => (
  <header className="bg-gradient-to-r from-slate-900 via-slate-800 to-slate-900 px-6 py-4 sticky top-0 z-50 shadow-xl border-b border-slate-700">
    <div className="flex items-center justify-between max-w-7xl mx-auto">
      <div className="flex items-center gap-4">
        <div className="relative">
          <div className="absolute inset-0 bg-orange-500 blur-lg opacity-50 rounded-2xl"></div>
          <div className="relative bg-gradient-to-br from-orange-500 to-orange-600 text-white p-3 rounded-2xl shadow-2xl">
            <i className="fas fa-oil-can text-xl"></i>
          </div>
        </div>
        <div>
          <h1 className="text-lg font-black text-white leading-none tracking-tight">PETROFAC</h1>
          <p className="text-[11px] text-orange-400 uppercase tracking-[0.15em] font-bold mt-0.5">Ain Tsila Lubrication System</p>
        </div>
      </div>
      <div className="flex items-center gap-4">
        <div className="flex items-center gap-2 bg-emerald-500/10 px-3 py-1.5 rounded-full border border-emerald-500/30">
          <span className="w-2 h-2 bg-emerald-400 rounded-full animate-pulse shadow-lg shadow-emerald-400/50"></span>
          <span className="text-[11px] font-bold text-emerald-400 uppercase tracking-wider">Live</span>
        </div>
        <button className="text-slate-400 hover:text-white transition-colors p-2 hover:bg-white/5 rounded-lg">
          <i className="fas fa-ellipsis-v"></i>
        </button>
      </div>
    </div>
  </header>
);

const SearchBar: React.FC<{ onSearch: (val: string) => void }> = ({ onSearch }) => (
  <div className="px-6 py-6 bg-gradient-to-b from-slate-900 to-slate-800">
    <div className="relative max-w-4xl mx-auto">
      <div className="absolute inset-0 bg-gradient-to-r from-orange-500/20 to-blue-500/20 blur-2xl rounded-3xl"></div>
      <div className="relative">
        <input 
          type="text" 
          placeholder="Search by Tag Number, System ID, or Equipment Description..." 
          className="w-full pl-14 pr-6 py-4 bg-slate-800/50 backdrop-blur-xl rounded-2xl text-sm text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-orange-500 transition-all border border-slate-700/50 focus:border-orange-500/50 shadow-2xl"
          onChange={(e) => onSearch(e.target.value)}
        />
        <div className="absolute left-5 top-1/2 -translate-y-1/2 text-orange-400">
          <i className="fas fa-search text-lg"></i>
        </div>
        <div className="absolute right-5 top-1/2 -translate-y-1/2 flex gap-2">
          <span className="text-[10px] font-bold text-slate-500 bg-slate-700/50 px-2 py-1 rounded uppercase">Ctrl+K</span>
        </div>
      </div>
    </div>
  </div>
);

const EquipmentCard: React.FC<{ equipment: EquipmentData; onClick: (eq: EquipmentData) => void }> = React.memo(({ equipment, onClick }) => (
  <div 
    className="group bg-gradient-to-br from-slate-800 to-slate-900 rounded-2xl p-5 border border-slate-700 hover:border-orange-500/50 active:scale-[0.98] transition-all cursor-pointer mb-4 hover:shadow-2xl hover:shadow-orange-500/10 relative overflow-hidden"
    onClick={() => onClick(equipment)}
  >
    <div className="absolute top-0 right-0 w-32 h-32 bg-gradient-to-br from-orange-500/5 to-transparent rounded-full -mr-16 -mt-16"></div>
    <div className="relative">
      <div className="flex justify-between items-start mb-3">
        <span className="text-[10px] font-black text-slate-500 bg-slate-700/50 px-3 py-1.5 rounded-lg uppercase tracking-wider border border-slate-600/50">{equipment.package}</span>
        <span className={`text-[10px] font-black px-3 py-1.5 rounded-lg uppercase border ${
          equipment.type === LubricantType.OIL 
            ? 'bg-blue-500/10 text-blue-400 border-blue-500/30' 
            : 'bg-emerald-500/10 text-emerald-400 border-emerald-500/30'
        }`}>
          <i className={`fas ${equipment.type === LubricantType.OIL ? 'fa-tint' : 'fa-fill-drip'} mr-1`}></i>
          {equipment.type}
        </span>
      </div>
      <h3 className="text-lg font-black text-white mb-2 group-hover:text-orange-400 transition-colors">{equipment.tagNo}</h3>
      <p className="text-sm text-slate-400 line-clamp-2 mb-4 leading-relaxed">{equipment.description}</p>
      <div className="flex items-center gap-6 text-xs text-slate-500 font-semibold border-t border-slate-700/50 pt-4">
        <div className="flex items-center gap-2">
          <i className="fas fa-flask text-orange-400"></i>
          <span className="text-slate-300">{equipment.grade}</span>
        </div>
        <div className="flex items-center gap-2">
          <i className="fas fa-clock text-blue-400"></i>
          <span className="text-slate-300">{equipment.replacementInterval || 'On Analysis'}</span>
        </div>
      </div>
    </div>
  </div>
));

const DetailView: React.FC<{ equipment: EquipmentData; onClose: () => void }> = ({ equipment, onClose }) => (
  <div className="fixed inset-0 bg-white z-[60] overflow-y-auto pb-20 animate-in slide-in-from-bottom duration-300">
    <div className="sticky top-0 bg-white/80 backdrop-blur-md p-4 border-b flex items-center gap-4 z-10">
      <button onClick={onClose} className="p-2 -ml-2 text-slate-600 hover:text-orange-600">
        <i className="fas fa-arrow-left"></i>
      </button>
      <div className="flex-1">
        <h2 className="font-bold text-slate-900 truncate leading-tight">{equipment.tagNo}</h2>
        <p className="text-[10px] text-slate-500 font-bold uppercase">{equipment.package}</p>
      </div>
    </div>

    <div className="p-4 space-y-6 max-w-lg mx-auto">
      <section className="bg-slate-50 p-4 rounded-2xl border border-slate-100">
        <h4 className="text-[10px] uppercase font-bold text-slate-400 mb-3 tracking-widest">Main Technical Data</h4>
        <div className="grid grid-cols-2 gap-4">
          <div>
            <p className="text-[10px] text-slate-500 mb-1">Description</p>
            <p className="text-xs font-semibold text-slate-900">{equipment.description}</p>
          </div>
          <div>
            <p className="text-[10px] text-slate-500 mb-1">Specific Part</p>
            <p className="text-xs font-semibold text-slate-900">{equipment.part}</p>
          </div>
        </div>
      </section>

      <section>
        <h4 className="text-[10px] uppercase font-bold text-slate-400 mb-3 tracking-widest">Lubrication Parameters</h4>
        <div className="space-y-1 bg-white border border-slate-100 rounded-2xl overflow-hidden shadow-sm">
          {[
            { label: 'Fluid Modality', val: equipment.type, icon: 'fa-tint' },
            { label: 'ISO/NLGI Grade', val: equipment.grade, icon: 'fa-vial' },
            { label: 'Initial Volume', val: equipment.initialFill, icon: 'fa-fill-drip' },
            { label: 'Top-Up Logic', val: equipment.topUpInterval, icon: 'fa-hourglass-half' },
            { label: 'Service Life', val: equipment.replacementInterval, icon: 'fa-redo' },
          ].map((item, idx) => (
            <div key={idx} className="flex justify-between items-center px-4 py-3 border-b last:border-0 border-slate-50 hover:bg-slate-50 transition-colors">
              <div className="flex items-center gap-3">
                <i className={`fas ${item.icon} text-slate-300 w-4 text-center`}></i>
                <span className="text-xs text-slate-600 font-medium">{item.label}</span>
              </div>
              <span className="text-xs font-bold text-slate-900">{item.val}</span>
            </div>
          ))}
        </div>
      </section>

      <section>
        <h4 className="text-[10px] uppercase font-bold text-slate-400 mb-3 tracking-widest">Equivalent Products</h4>
        <div className="grid grid-cols-1 gap-2">
          {Object.entries(equipment.brands).map(([brand, value]) => value && (
            <div key={brand} className="flex items-center gap-3 p-3 bg-white border border-slate-200 rounded-xl hover:border-orange-200 transition-all">
              <div className="w-10 h-10 rounded-lg bg-slate-50 flex items-center justify-center text-[10px] font-black text-slate-400 uppercase border border-slate-100">
                {brand.slice(0, 3)}
              </div>
              <div>
                <p className="text-[9px] text-slate-500 uppercase font-black tracking-tighter">{brand}</p>
                <p className="text-xs font-bold text-slate-900">{value}</p>
              </div>
            </div>
          ))}
        </div>
      </section>

      <section className="bg-orange-600 p-5 rounded-2xl shadow-lg shadow-orange-100 text-white">
        <h4 className="text-[10px] uppercase font-bold text-orange-200 mb-2 flex items-center gap-2">
          <i className="fas fa-info-circle"></i> Engineering Notes
        </h4>
        <p className="text-xs leading-relaxed font-medium">
          {equipment.remarks}
        </p>
      </section>
    </div>
  </div>
);

const AIExpert: React.FC = () => {
  const [query, setQuery] = useState('');
  const [selectedImage, setSelectedImage] = useState<string | null>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);
  const [messages, setMessages] = useState<{role: 'user' | 'bot', text: string, image?: string}[]>([
    {role: 'bot', text: "Engineering Department updated. The master database for Ain Tsila is now fully integrated. Ask me about any system (100, 301, 401, 800 series) or scan a technical manual page."}
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
    setMessages(prev => [...prev, { role: 'user', text: userMsg || "Analyzing scan...", image: userImg || undefined }]);
    setQuery('');
    setSelectedImage(null);
    setLoading(true);
    const botResponse = await askGemini(userMsg, userImg?.split(',')[1]);
    setMessages(prev => [...prev, { role: 'bot', text: botResponse || 'System error. Please retry.' }]);
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
              <span className="text-[10px] font-bold text-orange-600">Manual Scan Ready</span>
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
            placeholder="Search master tags or ask AI..." className="flex-1 px-4 py-3 bg-slate-100 rounded-xl text-sm focus:outline-none focus:ring-2 focus:ring-orange-600"
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

  const filteredEquipment = useMemo(() => {
    const term = searchTerm.toLowerCase().trim();
    if (!term) return EQUIPMENT_DATABASE;
    
    return EQUIPMENT_DATABASE.filter(item => {
      // Exact match for tagNo has priority
      if (item.tagNo.toLowerCase() === term) return true;
      
      // If search term looks like a tag (contains dash), only match exact tagNo
      if (term.includes('-')) {
        return item.tagNo.toLowerCase() === term;
      }
      
      // For non-tag searches, search in all fields
      return item.tagNo.toLowerCase().includes(term) ||
             item.description.toLowerCase().includes(term) ||
             item.package.toLowerCase().includes(term);
    });
  }, [searchTerm]);

  const displayedEquipment = useMemo(() => {
    return filteredEquipment
      .sort((a, b) => a.tagNo.localeCompare(b.tagNo, undefined, { numeric: true }))
      .slice(0, displayLimit);
  }, [filteredEquipment, displayLimit]);

  const renderContent = () => {
    switch (currentView) {
      case 'dashboard':
        return (
          <div className="p-6 space-y-6 bg-slate-900 min-h-screen">
            <div className="bg-gradient-to-br from-orange-500 via-orange-600 to-red-600 rounded-3xl p-8 text-white shadow-2xl relative overflow-hidden">
              <div className="absolute top-0 right-0 w-64 h-64 bg-white/5 rounded-full -mr-32 -mt-32"></div>
              <div className="absolute bottom-0 left-0 w-48 h-48 bg-black/10 rounded-full -ml-24 -mb-24"></div>
              <div className="relative z-10">
                <div className="flex justify-between items-start mb-8">
                  <div>
                    <p className="text-xs font-black uppercase tracking-[0.2em] text-orange-200 mb-2">System Overview</p>
                    <h2 className="text-3xl font-black leading-tight">Ain Tsila<br/>Lubrication Database</h2>
                  </div>
                  <div className="w-14 h-14 bg-white/10 backdrop-blur-xl rounded-2xl flex items-center justify-center border border-white/20 shadow-2xl">
                    <i className="fas fa-database text-2xl"></i>
                  </div>
                </div>
                <div className="grid grid-cols-2 gap-4">
                  <div className="bg-white/10 backdrop-blur-xl p-5 rounded-2xl border border-white/20 shadow-xl">
                    <p className="text-xs text-white/70 mb-2 font-bold uppercase tracking-wide">Total Equipment</p>
                    <p className="text-4xl font-black">{EQUIPMENT_DATABASE.length}</p>
                    <p className="text-[10px] text-white/60 mt-1">Active Tags</p>
                  </div>
                  <div className="bg-white/10 backdrop-blur-xl p-5 rounded-2xl border border-white/20 shadow-xl">
                    <p className="text-xs text-white/70 mb-2 font-bold uppercase tracking-wide">System Status</p>
                    <div className="flex items-center gap-2 mt-1">
                      <span className="w-3 h-3 bg-emerald-400 rounded-full animate-pulse shadow-lg shadow-emerald-400/50"></span>
                      <p className="text-xl font-black text-emerald-300">ONLINE</p>
                    </div>
                    <p className="text-[10px] text-white/60 mt-1">Fully Synced</p>
                  </div>
                </div>
              </div>
            </div>

            <section className="relative">
              <div className="flex items-center justify-between mb-5 px-1">
                <h3 className="text-sm font-black text-white uppercase tracking-[0.15em]">Recent Equipment</h3>
                <button onClick={() => setCurrentView('search')} className="text-xs font-bold text-orange-400 bg-orange-500/10 px-4 py-2 rounded-xl uppercase tracking-wider hover:bg-orange-500/20 transition-all border border-orange-500/20">
                  View All <i className="fas fa-arrow-right ml-2"></i>
                </button>
              </div>
              <div className="grid grid-cols-1 gap-4">
                {EQUIPMENT_DATABASE.slice(0, 6).map(eq => (
                  <EquipmentCard key={eq.id} equipment={eq} onClick={setSelectedEquipment} />
                ))}
              </div>
              <div className="absolute top-0 right-0 p-8 opacity-10 scale-150 rotate-12">
                <i className="fas fa-clipboard-list text-8xl"></i>
              </div>
            </section>
          </div>
        );
      case 'search':
        return (
          <div className="flex flex-col h-full overflow-hidden bg-slate-900">
            <SearchBar onSearch={setSearchTerm} />
            <div className="flex-1 overflow-y-auto p-6">
              <div className="flex justify-between items-center mb-6 sticky top-0 bg-slate-900 z-10 pb-4">
                <div>
                  <h2 className="text-xl font-black text-white">Equipment Registry</h2>
                  <p className="text-sm text-slate-400 mt-1">
                    {filteredEquipment.length} {filteredEquipment.length === 1 ? 'result' : 'results'} found
                  </p>
                </div>
                <button className="w-12 h-12 bg-slate-800 border border-slate-700 rounded-xl flex items-center justify-center hover:bg-slate-700 transition-all">
                  <i className="fas fa-sliders-h text-orange-400"></i>
                </button>
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
                    Load More ({filteredEquipment.length - displayedEquipment.length} remaining)
                  </button>
                </div>
              )}
              {filteredEquipment.length === 0 && (
                <div className="text-center py-32 px-12">
                  <div className="w-24 h-24 bg-slate-800 rounded-3xl flex items-center justify-center mx-auto mb-6 border border-slate-700">
                    <i className="fas fa-search-minus text-5xl text-slate-600"></i>
                  </div>
                  <h3 className="text-lg font-black text-white mb-3">No Equipment Found</h3>
                  <p className="text-sm text-slate-400 leading-relaxed max-w-md mx-auto">We couldn't find any equipment matching your search. Try using equipment tag numbers or system descriptions.</p>
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
    <div className="flex flex-col h-screen max-w-7xl mx-auto bg-slate-950 overflow-hidden font-sans">
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

      <nav className="fixed bottom-0 left-0 right-0 bg-slate-900/95 backdrop-blur-2xl border-t border-slate-700 py-5 px-12 z-40 max-w-7xl mx-auto shadow-2xl">
        <div className="flex justify-between items-center relative">
          {[
            { id: 'dashboard', icon: 'fa-home', label: 'Home' },
            { id: 'search', icon: 'fa-search', label: 'Search' },
            { id: 'ai', icon: 'fa-robot', label: 'AI Assistant' }
          ].map((item) => (
            <button 
              key={item.id}
              onClick={() => setCurrentView(item.id as ViewState)}
              className={`flex flex-col items-center gap-2 transition-all duration-300 relative group ${
                currentView === item.id ? 'text-orange-400 scale-110' : 'text-slate-500 hover:text-slate-300'
              }`}
            >
              <div className={`w-14 h-14 rounded-2xl flex items-center justify-center transition-all ${
                currentView === item.id 
                  ? 'bg-gradient-to-br from-orange-500 to-orange-600 shadow-2xl shadow-orange-500/50' 
                  : 'bg-slate-800 group-hover:bg-slate-700'
              }`}>
                <i className={`fas ${item.icon} text-xl ${currentView === item.id ? 'text-white' : 'text-slate-400'}`}></i>
              </div>
              <span className={`text-[10px] font-bold uppercase tracking-wider ${
                currentView === item.id ? 'opacity-100 text-orange-400' : 'opacity-70 text-slate-500'
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
