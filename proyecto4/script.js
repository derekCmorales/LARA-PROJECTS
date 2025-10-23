const nodeForm = document.getElementById("node-form");
const edgeForm = document.getElementById("edge-form");
const nodeInput = document.getElementById("node-name");
const edgeFromSelect = document.getElementById("edge-from");
const edgeToSelect = document.getElementById("edge-to");
const edgeWeightInput = document.getElementById("edge-weight");
const startNodeSelect = document.getElementById("start-node");
const runButton = document.getElementById("run-btn");
const resetButton = document.getElementById("reset-btn");
const exportButton = document.getElementById("export-btn");
const importButton = document.getElementById("import-btn");
const jsonTextarea = document.getElementById("graph-json");
const summaryDiv = document.getElementById("summary");
const resultDiv = document.getElementById("result");
const messageDiv = document.getElementById("message");

let nodes = new Set();
let edges = [];

const showMessage = (text, type = "success") => {
  messageDiv.textContent = text;
  messageDiv.className = type === "error" ? "error" : "success";
};

const formatWeight = (value) =>
  Number.isInteger(value) ? value.toString() : value.toFixed(2);

const clearMessage = () => {
  messageDiv.textContent = "";
  messageDiv.className = "";
};

const updateNodeSelects = () => {
  const options = ["<option value=\"\">Selecciona...</option>", ...[...nodes]
    .sort()
    .map((node) => `<option value="${node}">${node}</option>`)
  ];
  edgeFromSelect.innerHTML = options.join("");
  edgeToSelect.innerHTML = options.join("");
  startNodeSelect.innerHTML = options.join("");
};

const updateSummary = () => {
  if (!nodes.size) {
    summaryDiv.innerHTML = "<p>Agrega nodos y aristas para comenzar.</p>";
    return;
  }

  const nodesList = [...nodes]
    .sort()
    .map((node) => `<li><strong>${node}</strong></li>`)
    .join("");

  const edgesList = edges.length
    ? edges
        .map(
          (edge) =>
            `<li><span>${edge.from} → ${edge.to}</span><span>Peso: ${formatWeight(edge.weight)}</span></li>`
        )
        .join("")
    : "<li>Sin aristas registradas</li>";

  summaryDiv.innerHTML = `
    <div class="summary-grid">
      <div>
        <h3>Nodos (${nodes.size})</h3>
        <ul>${nodesList}</ul>
      </div>
      <div>
        <h3>Aristas (${edges.length})</h3>
        <ul class="edge-list">${edgesList}</ul>
      </div>
    </div>
  `;
};

const renderResult = (distances, previous, start) => {
  const nodeEntries = [...nodes].sort();
  if (!nodeEntries.length) {
    resultDiv.innerHTML = "";
    return;
  }

  const rows = nodeEntries
    .map((node) => {
      const distance = distances[node];
      const predecessor = previous[node] ?? "—";
      const path = buildPath(distances, previous, start, node);
      const pathText = path.length ? path.join(" → ") : "—";
      const formattedDistance = Number.isFinite(distance)
        ? distance.toFixed(2)
        : "∞";
      return `
        <tr>
          <td>${node}</td>
          <td>${formattedDistance}</td>
          <td>${predecessor}</td>
          <td>${pathText}</td>
        </tr>
      `;
    })
    .join("");

  resultDiv.innerHTML = `
    <table>
      <thead>
        <tr>
          <th>Nodo</th>
          <th>Distancia</th>
          <th>Predecesor</th>
          <th>Ruta</th>
        </tr>
      </thead>
      <tbody>${rows}</tbody>
    </table>
  `;
};

const buildPath = (distances, previous, start, target) => {
  if (!Number.isFinite(distances[target])) {
    return [];
  }
  const path = [];
  let current = target;
  const visited = new Set();
  while (current != null && !visited.has(current)) {
    path.unshift(current);
    visited.add(current);
    if (current === start) break;
    current = previous[current] ?? null;
  }
  return path;
};

const resetState = () => {
  nodes = new Set();
  edges = [];
  updateNodeSelects();
  updateSummary();
  resultDiv.innerHTML = "";
  jsonTextarea.value = "";
  clearMessage();
};

const validateWeight = (value) => {
  const weight = Number(value);
  if (!Number.isFinite(weight) || weight < 0) {
    throw new Error("El peso debe ser un número mayor o igual que 0.");
  }
  return weight;
};

nodeForm.addEventListener("submit", (event) => {
  event.preventDefault();
  const name = nodeInput.value.trim();
  if (!name) {
    showMessage("Ingresa un nombre de nodo válido.", "error");
    return;
  }
  if (nodes.has(name)) {
    showMessage(`El nodo "${name}" ya existe.`, "error");
    return;
  }
  nodes.add(name);
  nodeInput.value = "";
  updateNodeSelects();
  updateSummary();
  showMessage(`Nodo "${name}" agregado correctamente.`);
});

edgeForm.addEventListener("submit", (event) => {
  event.preventDefault();
  const from = edgeFromSelect.value;
  const to = edgeToSelect.value;
  if (!from || !to) {
    showMessage("Selecciona nodos de origen y destino.", "error");
    return;
  }
  if (from === to) {
    showMessage("El origen y el destino deben ser diferentes.", "error");
    return;
  }
  let weight;
  try {
    weight = validateWeight(edgeWeightInput.value);
  } catch (error) {
    showMessage(error.message, "error");
    return;
  }
  edges.push({ from, to, weight });
  edgeWeightInput.value = "";
  updateSummary();
  showMessage(`Arista ${from} → ${to} registrada.`);
});

runButton.addEventListener("click", () => {
  const start = startNodeSelect.value;
  if (!start) {
    showMessage("Selecciona un nodo de inicio.", "error");
    return;
  }
  if (!edges.length) {
    showMessage("Agrega al menos una arista para ejecutar el algoritmo.", "error");
    return;
  }
  const { distances, previous } = dijkstra([...nodes], edges, start);
  renderResult(distances, previous, start);
  showMessage("Algoritmo ejecutado correctamente.");
});

resetButton.addEventListener("click", () => {
  resetState();
  showMessage("Se reinició el grafo.");
});

exportButton.addEventListener("click", () => {
  const payload = {
    nodes: [...nodes],
    edges: edges.map((edge) => ({ ...edge })),
  };
  jsonTextarea.value = JSON.stringify(payload, null, 2);
  showMessage("Grafo exportado como JSON.");
});

importButton.addEventListener("click", () => {
  try {
    const payload = JSON.parse(jsonTextarea.value);
    if (!Array.isArray(payload.nodes) || !Array.isArray(payload.edges)) {
      throw new Error("Formato JSON inválido.");
    }
    const newNodes = new Set();
    payload.nodes.forEach((node) => {
      const trimmed = String(node).trim();
      if (!trimmed) {
        throw new Error("Los nodos importados deben tener un nombre válido.");
      }
      newNodes.add(trimmed);
    });
    const newEdges = payload.edges.map((edge) => {
      if (!edge || typeof edge.from !== "string" || typeof edge.to !== "string") {
        throw new Error("Cada arista debe tener campos 'from' y 'to'.");
      }
      const weight = validateWeight(edge.weight);
      const from = edge.from.trim();
      const to = edge.to.trim();
      if (!newNodes.has(from) || !newNodes.has(to)) {
        throw new Error("Las aristas deben referenciar nodos existentes.");
      }
      return { from, to, weight };
    });
    nodes = newNodes;
    edges = newEdges;
    updateNodeSelects();
    updateSummary();
    resultDiv.innerHTML = "";
    showMessage("Grafo importado correctamente.");
  } catch (error) {
    showMessage(`No fue posible importar el grafo: ${error.message}`, "error");
  }
});

const dijkstra = (nodeList, edgeList, start) => {
  const distances = {};
  const previous = {};
  nodeList.forEach((node) => {
    distances[node] = Infinity;
    previous[node] = null;
  });
  distances[start] = 0;

  const unvisited = new Set(nodeList);

  while (unvisited.size) {
    let current = null;
    let minDistance = Infinity;
    unvisited.forEach((node) => {
      if (distances[node] < minDistance) {
        minDistance = distances[node];
        current = node;
      }
    });

    if (current === null || minDistance === Infinity) {
      break;
    }

    unvisited.delete(current);

    edgeList
      .filter((edge) => edge.from === current)
      .forEach((edge) => {
        const alternate = distances[current] + edge.weight;
        if (alternate < distances[edge.to]) {
          distances[edge.to] = alternate;
          previous[edge.to] = current;
        }
      });
  }

  return { distances, previous };
};

updateNodeSelects();
updateSummary();
