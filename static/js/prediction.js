const apiUrl = "/predict-category-api/"; // Django endpoint for predictions

async function predictPhishingUrl(url) {
  try {
    const response = await fetch(apiUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
      body: new URLSearchParams({
        url: url,
      }),
    });

    if (!response.ok) {
      throw new Error(`Error: ${response.status}`);
    }

    const result = await response.json();
    console.log("Prediction:", result.prediction);
    console.log("Confidence Score:", result.confidence_score);

    // Update the DOM with the result
    document.getElementById(
      "prediction"
    ).innerText = `Prediction: ${result.prediction}`;
    document.getElementById(
      "confidence"
    ).innerText = `Confidence Score: ${result.confidence_score}`;
  } catch (error) {
    console.error("Error making the prediction:", error);
    document.getElementById("prediction").innerText =
      "Error occurred while making prediction";
  }
}

// Attach event listener to predict button
document.getElementById("submitBtn").addEventListener("click", () => {
  const url = document.getElementById("url-input").value;
  predictPhishingUrl(url);
});
