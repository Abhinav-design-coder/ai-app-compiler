import json
import os


TEMPLATE = """// Auto-generated React Application
// Configured Schemas:
__METADATA__

import React, { useState, useEffect } from 'react';

__PAGE_COMPONENTS__

export default function GeneratedApp() {
  const [currentPage, setCurrentPage] = useState('__FIRST_PAGE__');
  const [user, setUser] = useState(null);

  const handleLogin = (email) => {
    setUser({ email, role: 'admin' });
    setCurrentPage('__REDIRECT_PAGE__');
  };

  const handleLogout = () => {
    setUser(null);
    setCurrentPage('Login');
  };

  const renderPage = () => {
    switch (currentPage) {
__PAGE_CASES__
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
__PAGES_LIST_MAP__
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
"""

LOGIN_PAGE_TEMPLATE = """
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
"""

DASHBOARD_PAGE_TEMPLATE = """
function __NAME__Page() {
  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h2 className="text-3xl font-extrabold text-slate-800">__NAME__ Overview</h2>
        <span className="px-3 py-1 bg-green-100 text-green-800 rounded-full text-xs font-semibold">Live System</span>
      </div>
      
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="p-6 bg-white rounded-2xl shadow-sm border border-slate-100">
          <div className="text-slate-400 text-sm font-semibold uppercase tracking-wider">Database Tables</div>
          <div className="text-3xl font-bold text-slate-800 mt-2">__DB_TABLES_COUNT__</div>
          <div className="text-xs text-slate-500 mt-2">Active tables configured</div>
        </div>
        <div className="p-6 bg-white rounded-2xl shadow-sm border border-slate-100">
          <div className="text-slate-400 text-sm font-semibold uppercase tracking-wider">API Endpoints</div>
          <div className="text-3xl font-bold text-slate-800 mt-2">__API_ENDPOINTS_COUNT__</div>
          <div className="text-xs text-slate-500 mt-2">RESTful interfaces active</div>
        </div>
        <div className="p-6 bg-white rounded-2xl shadow-sm border border-slate-100">
          <div className="text-slate-400 text-sm font-semibold uppercase tracking-wider">Auth Roles</div>
          <div className="text-3xl font-bold text-slate-800 mt-2">__AUTH_ROLES_COUNT__</div>
          <div className="text-xs text-slate-500 mt-2">Defined permission levels</div>
        </div>
      </div>

      <div className="bg-white rounded-2xl p-6 shadow-sm border border-slate-100">
        <h3 className="text-lg font-bold text-slate-800 mb-4">Application Structure</h3>
        <div className="space-y-3 text-sm text-slate-600">
          <p>This is a compiled application based on your custom configuration schemas.</p>
          <div className="p-4 bg-slate-50 rounded-xl">
            <h4 className="font-semibold text-slate-700 mb-2">Available Tables & Schemas</h4>
            <ul className="list-disc pl-5 space-y-1">
__TABLES_LIST__
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
}
"""

CRUD_PAGE_TEMPLATE = """
function __NAME__Page() {
  const [items, setItems] = useState([]);
  const [newItem, setNewItem] = useState({ __FIELDS_STATE__ });

  useEffect(() => {
    fetch("http://localhost:8001/__API_PATH__")
      .then(res => res.json())
      .then(data => setItems(data));
  }, []);

  const handleAdd = (e) => {
    e.preventDefault();
    fetch("http://localhost:8001/__API_PATH__", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(newItem)
    })
      .then(res => res.json())
      .then(created => {
        setItems([...items, created]);
        setNewItem({ __FIELDS_STATE__ });
      });
  };

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h2 className="text-3xl font-extrabold text-slate-800">__NAME__ Management</h2>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className="lg:col-span-2 bg-white rounded-2xl p-6 shadow-sm border border-slate-100">
          <h3 className="text-lg font-bold text-slate-800 mb-4">Items List</h3>
          <div className="overflow-x-auto">
            <table className="w-full text-left border-collapse text-slate-650">
              <thead>
                <tr className="border-b border-slate-150 bg-slate-50 text-slate-500 text-xs font-semibold uppercase">
__TABLE_HEADERS__
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-100 text-sm text-slate-600">
                {items.map(item => (
                  <tr key={item.id} className="hover:bg-slate-50">
__TABLE_CELLS__
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>

        <div className="bg-white rounded-2xl p-6 shadow-sm border border-slate-100 h-fit">
          <h3 className="text-lg font-bold text-slate-800 mb-4">Add New __SINGULAR_NAME__</h3>
          <form onSubmit={handleAdd} className="space-y-4">
__FORM_INPUTS__
            <button type="submit" className="w-full py-2 bg-indigo-600 hover:bg-indigo-700 text-white font-semibold rounded-lg text-sm transition">
              Create
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}
"""

GENERIC_PAGE_TEMPLATE = """
function __NAME__Page() {
  return (
    <div className="bg-white rounded-2xl p-6 shadow-sm border border-slate-100">
      <h2 className="text-3xl font-extrabold text-slate-800 mb-4">__NAME__</h2>
      <p className="text-slate-500">Welcome to the generated __NAME__ page.</p>
    </div>
  );
}
"""

BUTTON_TEMPLATE = """            <button
              onClick={() => setCurrentPage('__PAGE_NAME__')}
              className={`w-full text-left py-2.5 px-4 rounded-xl text-sm font-semibold transition-all ${
                currentPage === '__PAGE_NAME__' 
                  ? 'bg-indigo-600 text-white shadow-md shadow-indigo-600/20' 
                  : 'text-slate-400 hover:bg-slate-800 hover:text-slate-200'
              }`}
            >
              __PAGE_NAME__
            </button>"""

def generate_react_app(schemas: dict) -> str:
    """
    Generates a complete React component representing the application based on the schema.
    """
    # Determine the absolute backend path based on the location of this file
    backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    generated_app_dir = os.path.join(backend_dir, "generated_app")
    os.makedirs(
        os.path.join(generated_app_dir, "src", "pages"),
        exist_ok=True
    )
    db_tables = schemas.get("database", {}).get("tables", [])
    api_endpoints = schemas.get("api", {}).get("endpoints", [])
    ui_pages = schemas.get("ui", {}).get("pages", [])
    auth_roles = schemas.get("auth", {}).get("roles", [])

    pages_list = [p.get("name", "") for p in ui_pages]
    
    # Collect metadata comments
    tables_info = []
    for table in db_tables:
        tables_info.append(f"// Table: {table.get('name')}, Fields: {', '.join(table.get('fields', []))}")
        
    endpoints_info = []
    for ep in api_endpoints:
        endpoints_info.append(f"// Endpoint: {ep.get('method')} {ep.get('path')}")
        
    roles_info = []
    for role in auth_roles:
        roles_info.append(f"// Role: {role.get('name')}, Permissions: {', '.join(role.get('permissions', []))}")

    metadata_str = "\n".join(tables_info + endpoints_info + roles_info)

    # Create page components
    page_components = []
    for page in ui_pages:
        name = page.get("name", "Page")
        if name.lower() == "login":
            page_components.append(LOGIN_PAGE_TEMPLATE)
        elif name.lower() in ["dashboard", "home", "analytics"]:
            tables_list = []
            for t in db_tables:
                tables_list.append(f"              <li><strong>{t.get('name')}</strong>: {', '.join(t.get('fields', []))}</li>")
            tables_list_str = "\n".join(tables_list)
            
            p_code = DASHBOARD_PAGE_TEMPLATE.replace("__NAME__", name)\
                                             .replace("__DB_TABLES_COUNT__", str(len(db_tables)))\
                                             .replace("__API_ENDPOINTS_COUNT__", str(len(api_endpoints)))\
                                             .replace("__AUTH_ROLES_COUNT__", str(len(auth_roles)))\
                                             .replace("__TABLES_LIST__", tables_list_str)
            page_components.append(p_code)
        else:
            # Generate a CRUD component if matching a database table
            table_match = None
            for t in db_tables:
                if t.get("name", "").lower() == name.lower() or t.get("name", "").lower() + "s" == name.lower() or name.lower() + "s" == t.get("name", "").lower():
                    table_match = t
                    break
            
            if table_match:
                fields = table_match.get("fields", ["id"])
                input_fields = [f for f in fields if f not in ["id", "password", "role"]]
                if not input_fields:
                    input_fields = fields
                
                fields_state = ", ".join([f"{f}: ''" for f in input_fields])
                
                form_inputs_list = []
                for f in input_fields:
                    inp = """          <div>
            <label className="block text-xs font-semibold text-slate-500 mb-1">__FIELD_CAPITALIZED__</label>
            <input 
              type="text" 
              value={newItem.__FIELD__} 
              onChange={e => setNewItem({...newItem, __FIELD__: e.target.value})} 
              className="w-full px-3 py-1.5 rounded-lg border border-slate-200 text-sm focus:outline-none focus:ring-1 focus:ring-indigo-500" 
              placeholder="Enter __FIELD__..."
            />
          </div>""".replace("__FIELD_CAPITALIZED__", f.capitalize())\
                     .replace("__FIELD__", f)
                    form_inputs_list.append(inp)
                form_inputs_str = "\n".join(form_inputs_list)
                
                mock_items = []
                if name.lower() == "contacts":
                    mock_items = [
                        {"id": 1, "name": "John Doe", "phone": "555-0199"},
                        {"id": 2, "name": "Jane Smith", "phone": "555-0144"}
                    ]
                elif name.lower() == "users":
                    mock_items = [
                        {"id": 1, "email": "admin@example.com", "role": "admin"},
                        {"id": 2, "email": "user@example.com", "role": "user"}
                    ]
                else:
                    mock_items = [
                        {"id": 1, **{f: f"{f}_val_1" for f in input_fields}},
                        {"id": 2, **{f: f"{f}_val_2" for f in input_fields}}
                    ]
                
                headers = ["                  <th className='p-3'>" + f.upper() + "</th>" for f in fields]
                headers_str = "\n".join(headers)
                
                cells = ["                    <td className='p-3'>{item." + f + "}</td>" for f in fields]
                cells_str = "\n".join(cells)
                
                singular_name = name[:-1] if name.endswith('s') else name
                
                p_code = CRUD_PAGE_TEMPLATE.replace("__NAME__", name)\
                                           .replace("__API_PATH__", table_match.get("name", ""))\
                                           .replace("__FIELDS_STATE__", fields_state)\
                                           .replace("__TABLE_HEADERS__", headers_str)\
                                           .replace("__TABLE_CELLS__", cells_str)\
                                           .replace("__SINGULAR_NAME__", singular_name)\
                                           .replace("__FORM_INPUTS__", form_inputs_str)
                page_components.append(p_code)
            else:
                p_code = GENERIC_PAGE_TEMPLATE.replace("__NAME__", name)
                page_components.append(p_code)

    page_components_str = "\n".join(page_components)
    first_page = pages_list[0] if pages_list else "Dashboard"
    
    # Generate page cases
    page_cases = []
    for p in pages_list:
        on_login_attr = " onLogin={handleLogin}" if p.lower() == "login" else ""
        page_cases.append(f"      case '{p}': return <{p}Page{on_login_attr} />;")
    page_cases_str = "\n".join(page_cases)

    # Generate page buttons map
    pages_list_map = []
    for p in pages_list:
        pages_list_map.append(BUTTON_TEMPLATE.replace("__PAGE_NAME__", p))
    pages_list_map_str = "\n".join(pages_list_map)

    non_login_pages = [p for p in pages_list if p.lower() != "login"]
    redirect_page = non_login_pages[0] if non_login_pages else "Dashboard"

    # Construct the final code
    code = TEMPLATE.replace("__METADATA__", metadata_str)\
                   .replace("__PAGE_COMPONENTS__", page_components_str)\
                   .replace("__FIRST_PAGE__", first_page)\
                   .replace("__REDIRECT_PAGE__", redirect_page)\
                   .replace("__PAGE_CASES__", page_cases_str)\
                   .replace("__PAGES_LIST_MAP__", pages_list_map_str)

    backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    generated_app_dir = os.path.join(backend_dir, "generated_app")
    output_dir = os.path.join(generated_app_dir, "src")

    os.makedirs(output_dir, exist_ok=True)

    package_json = """{
  "name": "generated-app",
  "private": true,
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "@vitejs/plugin-react": "^4.2.0",
    "autoprefixer": "^10.4.16",
    "postcss": "^8.4.31",
    "tailwindcss": "^3.3.5",
    "vite": "^5.0.0"
  }
}
"""

    with open(
        os.path.join(generated_app_dir, "package.json"),
        "w",
        encoding="utf-8"
    ) as f:
        f.write(package_json)

    index_html = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Generated App</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
"""

    with open(
        os.path.join(generated_app_dir, "index.html"),
        "w",
        encoding="utf-8"
    ) as f:
        f.write(index_html)

    vite_config = """import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
})
"""

    with open(
        os.path.join(generated_app_dir, "vite.config.js"),
        "w",
        encoding="utf-8"
    ) as f:
        f.write(vite_config)

    postcss_config = """export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
"""

    with open(
        os.path.join(generated_app_dir, "postcss.config.js"),
        "w",
        encoding="utf-8"
    ) as f:
        f.write(postcss_config)

    tailwind_config = """/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
"""

    with open(
        os.path.join(generated_app_dir, "tailwind.config.js"),
        "w",
        encoding="utf-8"
    ) as f:
        f.write(tailwind_config)

    with open(
        os.path.join(output_dir, "App.jsx"),
        "w",
        encoding="utf-8"
    ) as f:
        f.write(code)

    main_jsx = """
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import './index.css'

ReactDOM.createRoot(
  document.getElementById('root')
).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
)
"""

    with open(
        os.path.join(output_dir, "main.jsx"),
        "w",
        encoding="utf-8"
    ) as f:
        f.write(main_jsx)

    css = """
@tailwind base;
@tailwind components;
@tailwind utilities;
"""

    with open(
        os.path.join(output_dir, "index.css"),
        "w",
        encoding="utf-8"
    ) as f:
        f.write(css)

    return code
