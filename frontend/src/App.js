import React, { useState } from 'react';

function App() {
  const [products, setProducts] = useState([]);
  const [productForm, setProductForm] = useState({
    name: '',
    brand: '',
    product_type: '',
    presentation: ''
  });
  const [categoryName, setCategoryName] = useState('');
  const [categoryResult, setCategoryResult] = useState(null);
  const [routeStart, setRouteStart] = useState('');
  const [routeEnd, setRouteEnd] = useState('');
  const [routeResult, setRouteResult] = useState(null);
  const [addMsg, setAddMsg] = useState('');

  const handleInputChange = (e) => {
    setProductForm({...productForm, [e.target.name]: e.target.value});
  };

  const addProduct = async (e) => {
    e.preventDefault();
    const response = await fetch('/add_product/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(productForm)
    });
    const data = await response.json();
    if (data.message) {
      setAddMsg(data.message);
      setProductForm({name: '', brand: '', product_type: '', presentation: ''});
    } else {
      setAddMsg(data.error || 'Error añadiendo producto');
    }
  };

  const loadProducts = async () => {
    const response = await fetch('/list_products/');
    const data = await response.json();
    setProducts(data.products);
  };

  const searchCategory = async () => {
    if (!categoryName.trim()) return;
    const response = await fetch(`/search_category/?name=${encodeURIComponent(categoryName)}`);
    const data = await response.json();
    if (data.error) {
      setCategoryResult({error: data.error});
    } else {
      setCategoryResult(data);
    }
  };

  const calculateRoute = async () => {
    if (!routeStart || !routeEnd) return;
    const response = await fetch(`/calculate_route/?start=${encodeURIComponent(routeStart)}&end=${encodeURIComponent(routeEnd)}`);
    const data = await response.json();
    if (data.error) {
      setRouteResult({error: data.error});
    } else {
      setRouteResult(data);
    }
  };

  return (
    <div style={{padding: 20, fontFamily: 'Arial, sans-serif'}}>
      <h1>Guía para encontrar productos (React)</h1>

      <section style={{marginBottom: 30}}>
        <h2>Añadir producto</h2>
        <form onSubmit={addProduct}>
          <input name="name" value={productForm.name} onChange={handleInputChange} placeholder="Nombre" required />
          <input name="brand" value={productForm.brand} onChange={handleInputChange} placeholder="Marca" required />
          <input name="product_type" value={productForm.product_type} onChange={handleInputChange} placeholder="Tipo" required />
          <input name="presentation" value={productForm.presentation} onChange={handleInputChange} placeholder="Presentación" required />
          <button type="submit">Añadir</button>
        </form>
        {addMsg && <p>{addMsg}</p>}
      </section>

      <section style={{marginBottom: 30}}>
        <h2>Lista de productos</h2>
        <button onClick={loadProducts}>Cargar Productos</button>
        <ul>
          {products.map((p, idx) => (
            <li key={idx}>{p.name} - {p.brand} - {p.product_type} - {p.presentation}</li>
          ))}
        </ul>
      </section>

      <section style={{marginBottom: 30}}>
        <h2>Buscar categoría</h2>
        <input value={categoryName} onChange={(e) => setCategoryName(e.target.value)} placeholder="Nombre categoría" />
        <button onClick={searchCategory}>Buscar</button>
        <div>
          {categoryResult ? (
            categoryResult.error ? (
              <p>{categoryResult.error}</p>
            ) : (
              <div>
                <p>Categoría: {categoryResult.category}</p>
                <p>Hijos:</p>
                <ul>
                  {categoryResult.children.map((child, i) => (
                    <li key={i}>{child}</li>
                  ))}
                </ul>
              </div>
            )
          ) : null}
        </div>
      </section>

      <section style={{marginBottom: 30}}>
        <h2>Calcular ruta óptima</h2>
        <select value={routeStart} onChange={e => setRouteStart(e.target.value)}>
          <option value="">Pasillo inicio</option>
          <option value="Pasillo 1">Pasillo 1</option>
          <option value="Pasillo 2">Pasillo 2</option>
          <option value="Pasillo 3">Pasillo 3</option>
          <option value="Pasillo 4">Pasillo 4</option>
          <option value="Pasillo 5">Pasillo 5</option>
          <option value="Pasillo 6">Pasillo 6</option>
        </select>
        <select value={routeEnd} onChange={e => setRouteEnd(e.target.value)}>
          <option value="">Pasillo destino</option>
          <option value="Pasillo 1">Pasillo 1</option>
          <option value="Pasillo 2">Pasillo 2</option>
          <option value="Pasillo 3">Pasillo 3</option>
          <option value="Pasillo 4">Pasillo 4</option>
          <option value="Pasillo 5">Pasillo 5</option>
          <option value="Pasillo 6">Pasillo 6</option>
        </select>
        <button onClick={calculateRoute}>Calcular Ruta</button>
        <div>
          {routeResult ? (
            routeResult.error ? (
              <p>{routeResult.error}</p>
            ) : (
              <p>Ruta: {routeResult.route.join(' -> ')}</p>
            )
          ) : null}
        </div>
      </section>
    </div>
  );
}

export default App;
