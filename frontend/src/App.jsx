import './index.css';
import { useState } from 'react';

export default function App() {
  const [prompt, setPrompt] = useState('');
  const [loading, setLoading] = useState(false);
  const [output, setOutput] = useState(null);
  const [error, setError] = useState(null);

  const handleGenerate = async () => {
    if (!prompt.trim()) {
      setError('Please enter a prompt');
      return;
    }

    setLoading(true);
    setError(null);
    setOutput(null);

    try {
      const response = await fetch('http://localhost:8000/compile', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ prompt }),
      });

      if (!response.ok) {
        throw new Error(`API error: ${response.statusText}`);
      }

      const data = await response.json();
      setOutput(data);
    } catch (err) {
      setError(err.message || 'Failed to generate architecture');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleClear = () => {
    setPrompt('');
    setOutput(null);
    setError(null);
  };

  return (
    <div className="min-h-screen bg-gradient flex items-center justify-center p-4">
      <div className="w-full max-w-4xl">
        {/* Header */}
        <div className="text-center mb-8">
          <h1 className="text-5xl font-bold text-white mb-2">
            AI App Compiler
          </h1>
          <p className="text-white/80 text-lg">
            Generate complete app architectures from natural language prompts
          </p>
        </div>

        {/* Main Card */}
        <div className="glass-card p-8 shadow-2xl">
          {/* Input Section */}
          <div className="mb-6">
            <label className="block text-slate-700 font-semibold mb-3">
              Describe Your Application
            </label>
            <textarea
              value={prompt}
              onChange={(e) => setPrompt(e.target.value)}
              placeholder="e.g., Build a CRM with contacts and dashboard..."
              className="glass-input w-full p-4 rounded-lg text-slate-900 placeholder-slate-400 min-h-24 resize-none focus:ring-2 focus:ring-offset-0"
              disabled={loading}
            />
          </div>

          {/* Error Message */}
          {error && (
            <div className="mb-6 p-4 bg-red-100 border border-red-300 text-red-700 rounded-lg">
              {error}
            </div>
          )}

          {/* Buttons */}
          <div className="flex gap-3 mb-8">
            <button
              onClick={handleGenerate}
              disabled={loading}
              className="glass-button flex-1 py-3 px-6 font-semibold text-white rounded-lg disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {loading ? (
                <span className="flex items-center justify-center gap-2">
                  <svg className="animate-spin h-5 w-5" viewBox="0 0 24 24">
                    <circle className="opacity-25" cx="12" cy="12" r="10" fill="none" stroke="currentColor" strokeWidth="4" />
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
                  </svg>
                  Generating...
                </span>
              ) : (
                'Generate Architecture'
              )}
            </button>
            {prompt && (
              <button
                onClick={handleClear}
                disabled={loading}
                className="py-3 px-6 font-semibold text-slate-700 rounded-lg glass-input hover:bg-slate-100 transition disabled:opacity-50 disabled:cursor-not-allowed"
              >
                Clear
              </button>
            )}
          </div>

          {/* Output Section */}
          {output && (
            <div className="mt-8">
              <h2 className="text-slate-700 font-semibold mb-4">Generated Output</h2>
              <div className="grid grid-cols-1 lg:grid-cols-2 gap-4 mb-6">
                {/* Intent */}
                <div className="glass-card p-4">
                  <h3 className="text-slate-700 font-semibold mb-2 text-sm">Intent</h3>
                  <pre className="json-output p-3 text-xs max-h-40 overflow-auto">
                    {JSON.stringify(output.intent, null, 2)}
                  </pre>
                </div>

                {/* Architecture */}
                <div className="glass-card p-4">
                  <h3 className="text-slate-700 font-semibold mb-2 text-sm">Architecture</h3>
                  <pre className="json-output p-3 text-xs max-h-40 overflow-auto">
                    {JSON.stringify(output.architecture, null, 2)}
                  </pre>
                </div>
              </div>

              {/* Validation & Repairs */}
              <div className="grid grid-cols-1 lg:grid-cols-2 gap-4 mb-6">
                {/* Validation */}
                <div className="glass-card p-4">
                  <h3 className="text-slate-700 font-semibold mb-2 text-sm flex items-center gap-2">
                    <span className={output.validation.valid ? 'text-green-600' : 'text-amber-600'}>
                      ●
                    </span>
                    Validation
                  </h3>
                  <pre className="json-output p-3 text-xs max-h-40 overflow-auto">
                    {JSON.stringify(output.validation, null, 2)}
                  </pre>
                </div>

                {/* Repairs */}
                <div className="glass-card p-4">
                  <h3 className="text-slate-700 font-semibold mb-2 text-sm">Repairs Applied</h3>
                  <div className="space-y-1">
                    {output.repairs && output.repairs.length > 0 ? (
                      output.repairs.map((repair, idx) => (
                        <div key={idx} className="text-slate-600 text-sm flex items-center gap-2">
                          <span className="text-green-600">✓</span>
                          {repair}
                        </div>
                      ))
                    ) : (
                      <div className="text-slate-500 text-sm">No repairs needed</div>
                    )}
                  </div>
                </div>
              </div>

              {/* Runtime & Schemas */}
              <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
                {/* Runtime */}
                <div className="glass-card p-4">
                  <h3 className="text-slate-700 font-semibold mb-2 text-sm flex items-center gap-2">
                    <span className={output.runtime.deployable ? 'text-green-600' : 'text-red-600'}>
                      ●
                    </span>
                    Runtime Status
                  </h3>
                  <pre className="json-output p-3 text-xs max-h-40 overflow-auto">
                    {JSON.stringify(output.runtime, null, 2)}
                  </pre>
                </div>

                {/* Full Schemas */}
                <div className="glass-card p-4">
                  <h3 className="text-slate-700 font-semibold mb-2 text-sm">Generated Schemas</h3>
                  <pre className="json-output p-3 text-xs max-h-40 overflow-auto">
                    {JSON.stringify(output.schemas, null, 2)}
                  </pre>
                </div>
              </div>
            </div>
          )}
        </div>

        {/* Footer */}
        <div className="text-center mt-8 text-white/60 text-sm">
          Powered by AI App Compiler • Backend running on http://localhost:8000
        </div>
      </div>
    </div>
  );
}
