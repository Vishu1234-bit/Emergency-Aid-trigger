// frontend/script.js
async function verifyDisaster() {
  const type = document.getElementById("disasterType").value;
  const location = document.getElementById("location").value;
  const source = document.getElementById("source").value;

  const response = await fetch("http://127.0.0.1:5000/verify_news", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ type, location, source })
  });

  const data = await response.json();

  const result = document.getElementById("result");
  if (data.is_valid) {
    result.innerHTML = `✅ Valid Disaster! Confidence: ${data.confidence}`;
    document.getElementById("triggerBtn").style.display = "block";
  } else {
    result.innerHTML = `❌ Not valid. Confidence: ${data.confidence}`;
    document.getElementById("triggerBtn").style.display = "none";
  }
}

async function triggerFund() {
  const response = await fetch("http://127.0.0.1:5000/trigger_fund", {
    method: "POST"
  });

  const data = await response.json();
  alert("✅ Funds Released! Txn: " + data.txn);
}
