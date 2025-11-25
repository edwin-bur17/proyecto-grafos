/**
 * Shopping Cart - Manejo de selección de productos con persistencia
 * Mantiene las selecciones de productos cuando se aplican filtros
 * Usa sessionStorage para que la persistencia se limpie al cerrar la sesión
 */

// Clave para sessionStorage
const STORAGE_KEY = "productos_seleccionados";

/**
 * Obtiene las selecciones guardadas desde sessionStorage
 */
function getStoredSelections() {
  try {
    const stored = sessionStorage.getItem(STORAGE_KEY);
    return stored ? JSON.parse(stored) : [];
  } catch (error) {
    console.error("Error al cargar selecciones:", error);
    return [];
  }
}

/**
 * Guarda las selecciones actuales en sessionStorage
 */
function saveSelections(selections) {
  try {
    sessionStorage.setItem(STORAGE_KEY, JSON.stringify(selections));
  } catch (error) {
    console.error("Error al guardar selecciones:", error);
  }
}

/**
 * Obtiene todas las selecciones actuales desde los checkboxes
 */
function getCurrentSelections() {
  const checkboxes = document.querySelectorAll(
    'input[name="productos"]:checked'
  );
  return Array.from(checkboxes).map((cb) => cb.value);
}

/**
 * Restaura las selecciones desde sessionStorage al cargar la página
 */
function restoreSelections() {
  const storedSelections = getStoredSelections();
  const checkboxes = document.querySelectorAll('input[name="productos"]');

  checkboxes.forEach((checkbox) => {
    if (storedSelections.includes(checkbox.value)) {
      checkbox.checked = true;
    }
  });
}

/**
 * Actualiza las selecciones cuando cambia un checkbox
 */
function handleCheckboxChange() {
  const selections = getCurrentSelections();
  saveSelections(selections);
}

/**
 * Limpia todas las selecciones
 */
function clearSelections() {
  sessionStorage.removeItem(STORAGE_KEY);
}

/**
 * Inicializa los event listeners
 */
function initializeShoppingCart() {
  // Limpiar localStorage antiguo (migración de versión anterior)
  localStorage.removeItem(STORAGE_KEY);
  
  // Restaurar selecciones al cargar
  restoreSelections();

  // Agregar listeners a todos los checkboxes
  const checkboxes = document.querySelectorAll('input[name="productos"]');
  checkboxes.forEach((checkbox) => {
    checkbox.addEventListener("change", handleCheckboxChange);
  });

  // Handler para el botón de limpiar selección
  const clearButton = document.querySelector('a[href*="limpiar-seleccion"]');
  if (clearButton) {
    clearButton.addEventListener("click", function (e) {
      clearSelections();
      // Desmarcar todos los checkboxes inmediatamente
      const checkboxes = document.querySelectorAll('input[name="productos"]');
      checkboxes.forEach((checkbox) => {
        checkbox.checked = false;
      });
    });
  }

  // Handler para sincronizar selecciones antes de enviar el formulario de ruta
  const routeForm = document.querySelector('form[action*="calcular_ruta"]');
  if (routeForm) {
    routeForm.addEventListener("submit", function () {
      // Actualizar sessionStorage antes de enviar
      const selections = getCurrentSelections();
      saveSelections(selections);
    });
  }

  // Handler para sincronizar selecciones antes de aplicar filtros/búsqueda
  const searchForm = document.querySelector('form[action*="inicio"]');
  if (searchForm) {
    searchForm.addEventListener("submit", function () {
      // Guardar selecciones actuales antes de filtrar
      const selections = getCurrentSelections();
      saveSelections(selections);
    });
  }
}

// Inicializar cuando el DOM esté listo
if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initializeShoppingCart);
} else {
  initializeShoppingCart();
}
