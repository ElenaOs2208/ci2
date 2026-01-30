document.getElementById("search-form")
  .addEventListener("submit", async function (event) {
    event.preventDefault();

    const smiles = document.getElementById("smiles-input").value;

    const response = await fetch("/api/search", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ smiles: smiles })
    });

    const data = await response.json();

    document.getElementById("status").innerHTML =
      "<strong>SMILES:</strong> " + data.smiles + "<br>" +
      "<strong>Formula:</strong> " + data.formula + "<br>" +
      "<strong>Molecular weight:</strong> " + data.weight +
      "<br><br>" +
      "<img src='" + data.image + "' width='400'>";
});

