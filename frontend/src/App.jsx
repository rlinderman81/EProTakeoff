import { useState } from 'react'
import axios from 'axios'

function App() {
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [result, setResult] = useState(null);

  const onFileChange = (e) => {
    const f = e.target.files[0];
    setFile(f);
    setPreview(URL.createObjectURL(f));
    setResult(null);
  };

  const runDetection = async () => {
    if (!file) return;
    const form = new FormData();
    form.append('file', file);
    const { data } = await axios.post('http://localhost:8000/upload', form, {
      headers: { 'Content-Type': 'multipart/form-data' },
    });
    setResult(data);
  };

  return (
    <div className="p-4 max-w-4xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">Lighting Takeoff MVP</h1>

      <input type="file" accept="image/*,.pdf" onChange={onFileChange} className="mb-4" />

      {preview && (
        <div className="my-4">
          <img src={preview} alt="plan preview" className="max-h-96 border" />
        </div>
      )}

      <button
        className="px-4 py-2 bg-blue-600 text-white rounded mb-4"
        onClick={runDetection}
        disabled={!file}
      >
        {file ? 'Run Detection' : 'Select a File First'}
      </button>

      {result && (
        <div className="bg-gray-100 p-4 rounded">
          <h2 className="font-semibold mb-2">Results</h2>
          <p>Total lights detected: <strong>{result.count}</strong></p>
          <pre className="text-xs overflow-x-auto">{JSON.stringify(result.detections, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default App;