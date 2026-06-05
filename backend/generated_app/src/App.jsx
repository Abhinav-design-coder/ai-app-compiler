// Auto-generated React Application
// Configured Schemas:
// Table: users, Fields: id, email, password, role
// Table: products, Fields: id, name, price, stock
// Table: managements, Fields: id, name, description
// Endpoint: POST /login
// Endpoint: GET /products
// Endpoint: GET /managements
// Role: admin, Permissions: full_access
// Role: user, Permissions: basic_access

import React, { useState, useEffect } from 'react';


function LoginPage({ onLogin }) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (email && password) {
      onLogin(email);
    } else {
      setError('Please fill in all fields');
    }
  };

  return (
    <div className="max-w-md mx-auto my-12 p-8 bg-white rounded-2xl shadow-xl border border-slate-100">
      <h2 className="text-3xl font-extrabold text-slate-800 mb-6 text-center">Sign In</h2>
      {error && <div className="mb-4 p-3 bg-red-50 text-red-600 rounded-lg text-sm">{error}</div>}
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block text-sm font-semibold text-slate-600 mb-1">Email Address</label>
          <input 
            type="email" 
            value={email} 
            onChange={e => setEmail(e.target.value)} 
            className="w-full px-4 py-2.5 rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-indigo-500" 
            placeholder="admin@example.com"
          />
        </div>
        <div>
          <label className="block text-sm font-semibold text-slate-600 mb-1">Password</label>
          <input 
            type="password" 
            value={password} 
            onChange={e => setPassword(e.target.value)} 
            className="w-full px-4 py-2.5 rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-indigo-500" 
            placeholder="••••••••"
          />
        </div>
        <button type="submit" className="w-full py-3 bg-indigo-600 hover:bg-indigo-700 text-white font-bold rounded-xl transition duration-200">
          Continue
        </button>
      </form>
    </div>
  );
}


function AuthPage() {
  return (
    <div className="bg-white rounded-2xl p-6 shadow-sm border border-slate-100">
      <h2 className="text-3xl font-extrabold text-slate-800 mb-4">Auth</h2>
      <p className="text-slate-500">Welcome to the generated Auth page.</p>
    </div>
  );
}


function ManagementsPage() {
  const API_URL = "http://localhost:8001/managements";
  const [items, setItems] = useState([]);
  useEffect(() => {
    fetch(API_URL)
      .then(res => res.json())
      .then(data => setItems(data))
      .catch(err => console.error(err));
  }, []);
  const [newItem, setNewItem] = useState({ name: '', description: '' });

  const handleAdd = (e) => {
    e.preventDefault();
    fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(newItem)
    })
      .then(res => res.json())
      .then(created => {
        setItems([...items, created]);
        setNewItem({ name: '', description: '' });
      });
  };

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h2 className="text-3xl font-extrabold text-slate-800">Managements Management</h2>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className="lg:col-span-2 bg-white rounded-2xl p-6 shadow-sm border border-slate-100">
          <h3 className="text-lg font-bold text-slate-800 mb-4">Items List</h3>
          <div className="overflow-x-auto">
            <table className="w-full text-left border-collapse text-slate-650">
              <thead>
                <tr className="border-b border-slate-150 bg-slate-50 text-slate-500 text-xs font-semibold uppercase">
                  <th className='p-3'>ID</th>
                  <th className='p-3'>NAME</th>
                  <th className='p-3'>DESCRIPTION</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-100 text-sm text-slate-600">
                {items.map(item => (
                  <tr key={item.id} className="hover:bg-slate-50">
                    <td className='p-3'>{item.id}</td>
                    <td className='p-3'>{item.name}</td>
                    <td className='p-3'>{item.description}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>

        <div className="bg-white rounded-2xl p-6 shadow-sm border border-slate-100 h-fit">
          <h3 className="text-lg font-bold text-slate-800 mb-4">Add New Management</h3>
          <form onSubmit={handleAdd} className="space-y-4">
          <div>
            <label className="block text-xs font-semibold text-slate-500 mb-1">Name</label>
            <input 
              type="text" 
              value={newItem.name} 
              onChange={e => setNewItem({...newItem, name: e.target.value})} 
              className="w-full px-3 py-1.5 rounded-lg border border-slate-200 text-sm focus:outline-none focus:ring-1 focus:ring-indigo-500" 
              placeholder="Enter name..."
            />
          </div>
          <div>
            <label className="block text-xs font-semibold text-slate-500 mb-1">Description</label>
            <input 
              type="text" 
              value={newItem.description} 
              onChange={e => setNewItem({...newItem, description: e.target.value})} 
              className="w-full px-3 py-1.5 rounded-lg border border-slate-200 text-sm focus:outline-none focus:ring-1 focus:ring-indigo-500" 
              placeholder="Enter description..."
            />
          </div>
            <button type="submit" className="w-full py-2 bg-indigo-600 hover:bg-indigo-700 text-white font-semibold rounded-lg text-sm transition">
              Create
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}


function ProductsPage() {
  const API_URL = "http://localhost:8001/products";
  const [items, setItems] = useState([]);
  useEffect(() => {
    fetch(API_URL)
      .then(res => res.json())
      .then(data => setItems(data))
      .catch(err => console.error(err));
  }, []);
  const [newItem, setNewItem] = useState({ name: '', price: '', stock: '' });

  const handleAdd = (e) => {
    e.preventDefault();
    fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(newItem)
    })
      .then(res => res.json())
      .then(created => {
        setItems([...items, created]);
        setNewItem({ name: '', price: '', stock: '' });
      });
  };

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h2 className="text-3xl font-extrabold text-slate-800">Products Management</h2>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className="lg:col-span-2 bg-white rounded-2xl p-6 shadow-sm border border-slate-100">
          <h3 className="text-lg font-bold text-slate-800 mb-4">Items List</h3>
          <div className="overflow-x-auto">
            <table className="w-full text-left border-collapse text-slate-650">
              <thead>
                <tr className="border-b border-slate-150 bg-slate-50 text-slate-500 text-xs font-semibold uppercase">
                  <th className='p-3'>ID</th>
                  <th className='p-3'>NAME</th>
                  <th className='p-3'>PRICE</th>
                  <th className='p-3'>STOCK</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-100 text-sm text-slate-600">
                {items.map(item => (
                  <tr key={item.id} className="hover:bg-slate-50">
                    <td className='p-3'>{item.id}</td>
                    <td className='p-3'>{item.name}</td>
                    <td className='p-3'>{item.price}</td>
                    <td className='p-3'>{item.stock}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>

        <div className="bg-white rounded-2xl p-6 shadow-sm border border-slate-100 h-fit">
          <h3 className="text-lg font-bold text-slate-800 mb-4">Add New Product</h3>
          <form onSubmit={handleAdd} className="space-y-4">
          <div>
            <label className="block text-xs font-semibold text-slate-500 mb-1">Name</label>
            <input 
              type="text" 
              value={newItem.name} 
              onChange={e => setNewItem({...newItem, name: e.target.value})} 
              className="w-full px-3 py-1.5 rounded-lg border border-slate-200 text-sm focus:outline-none focus:ring-1 focus:ring-indigo-500" 
              placeholder="Enter name..."
            />
          </div>
          <div>
            <label className="block text-xs font-semibold text-slate-500 mb-1">Price</label>
            <input 
              type="text" 
              value={newItem.price} 
              onChange={e => setNewItem({...newItem, price: e.target.value})} 
              className="w-full px-3 py-1.5 rounded-lg border border-slate-200 text-sm focus:outline-none focus:ring-1 focus:ring-indigo-500" 
              placeholder="Enter price..."
            />
          </div>
          <div>
            <label className="block text-xs font-semibold text-slate-500 mb-1">Stock</label>
            <input 
              type="text" 
              value={newItem.stock} 
              onChange={e => setNewItem({...newItem, stock: e.target.value})} 
              className="w-full px-3 py-1.5 rounded-lg border border-slate-200 text-sm focus:outline-none focus:ring-1 focus:ring-indigo-500" 
              placeholder="Enter stock..."
            />
          </div>
            <button type="submit" className="w-full py-2 bg-indigo-600 hover:bg-indigo-700 text-white font-semibold rounded-lg text-sm transition">
              Create
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}


export default function GeneratedApp() {
  const [currentPage, setCurrentPage] = useState('Login');
  const [user, setUser] = useState(null);

  const handleLogin = (email) => {
    setUser({ email, role: 'admin' });
    setCurrentPage('Auth');
  };

  const handleLogout = () => {
    setUser(null);
    setCurrentPage('Login');
  };

  const renderPage = () => {
    switch (currentPage) {
      case 'Login': return <LoginPage onLogin={handleLogin} />;
      case 'Auth': return <AuthPage />;
      case 'Managements': return <ManagementsPage />;
      case 'Products': return <ProductsPage />;
      default: return <div className="p-6">Page not found</div>;
    }
  };

  return (
    <div className="min-h-screen bg-slate-50 flex">
      {/* Sidebar Navigation */}
      <aside className="w-64 bg-slate-900 text-slate-100 p-6 flex flex-col justify-between">
        <div>
          <div className="flex items-center gap-2 mb-8 px-2">
            <span className="text-2xl">⚡</span>
            <span className="font-extrabold text-lg tracking-wider text-white">GEN-APP</span>
          </div>
          <nav className="space-y-1">
            <button
              onClick={() => setCurrentPage('Login')}
              className={`w-full text-left py-2.5 px-4 rounded-xl text-sm font-semibold transition-all ${
                currentPage === 'Login' 
                  ? 'bg-indigo-600 text-white shadow-md shadow-indigo-600/20' 
                  : 'text-slate-400 hover:bg-slate-800 hover:text-slate-200'
              }`}
            >
              Login
            </button>
            <button
              onClick={() => setCurrentPage('Auth')}
              className={`w-full text-left py-2.5 px-4 rounded-xl text-sm font-semibold transition-all ${
                currentPage === 'Auth' 
                  ? 'bg-indigo-600 text-white shadow-md shadow-indigo-600/20' 
                  : 'text-slate-400 hover:bg-slate-800 hover:text-slate-200'
              }`}
            >
              Auth
            </button>
            <button
              onClick={() => setCurrentPage('Managements')}
              className={`w-full text-left py-2.5 px-4 rounded-xl text-sm font-semibold transition-all ${
                currentPage === 'Managements' 
                  ? 'bg-indigo-600 text-white shadow-md shadow-indigo-600/20' 
                  : 'text-slate-400 hover:bg-slate-800 hover:text-slate-200'
              }`}
            >
              Managements
            </button>
            <button
              onClick={() => setCurrentPage('Products')}
              className={`w-full text-left py-2.5 px-4 rounded-xl text-sm font-semibold transition-all ${
                currentPage === 'Products' 
                  ? 'bg-indigo-600 text-white shadow-md shadow-indigo-600/20' 
                  : 'text-slate-400 hover:bg-slate-800 hover:text-slate-200'
              }`}
            >
              Products
            </button>
          </nav>
        </div>
        
        {/* User Info / Footer */}
        <div className="border-t border-slate-800 pt-4 px-2">
          {user ? (
            <div className="flex items-center justify-between text-xs">
              <div className="text-xs">
                <div className="font-bold text-white truncate max-w-[120px]">{user.email}</div>
                <div className="text-slate-500 capitalize">{user.role}</div>
              </div>
              <button 
                onClick={handleLogout} 
                className="text-xs text-indigo-400 hover:text-indigo-300 font-semibold"
              >
                Logout
              </button>
            </div>
          ) : (
            <div className="text-xs text-slate-500">Not signed in</div>
          )}
        </div>
      </aside>

      {/* Main Content Area */}
      <main className="flex-1 p-10 overflow-y-auto">
        {renderPage()}
      </main>
    </div>
  );
}
