# Beginner-Friendly Guide: Vision‑LLM Handwriting Translation

## 1. Experimental Matrix (Overview of Models)
---
| Term         | Plain English Explanation                                      |
|--------------|---------------------------------------------------------------|
| **Model**    | The specific AI “brain” you’re testing (e.g. Llama‑4 Scout).   |
| **Params**   | Short for “parameters.” Think of these as the number of knobs inside the model—it shows how much it has “learned.” |
| **Input Size** | How much of the handwritten image you feed in at once (here, one line of text). |
| **Batch**    | How many images you process in a single go. Batch 1 = one image at a time. |
| **Notes**    | Extra tips (e.g. bigger models tend to be slower).            |
---

## 2. Inference Pipeline (How We Go from Image → Translation)

1. **Preprocessing**  
   - **Grayscale:** Turn the image into black‑and‑white so the model focuses on shapes, not colors.  
   - **Deskew:** Straighten any tilted images.  
   - **Resize:** Make the shorter side of the image 480 px tall so all images are the same size.

2. **Prompt Template**  
   > “Translate exactly what is written in this image into German. Do not add, remove, or invent any information.”

3. **Model Invocation**  
   - Send the cleaned image + prompt to the model (via API or local runtime).  
   - Receive the model’s text output.

4. **Post‑Processing**  
   - **Strip whitespace:** Remove extra spaces at the start/end of the text.  
   - **Normalize punctuation:** Make commas, periods, quotes, etc., consistent.  
   - **Detokenize (if needed):** Rejoin word pieces that some models split apart.

---

## 3. Metrics Collection (How We Measure Success)
---
| Metric       | What It Tells You                                       |
|--------------|---------------------------------------------------------|
| **BLEU‑4**   | (0–1) How many of the model’s 4‑word sequences match the human translation. Higher is better. |
| **CHRF**     | (0–1) Looks at matches at the character level—good for long or compound words. Higher is better. |
| **TER**      | (% edits) How many insertions/deletions/swaps are needed to turn the model’s output into the reference. Lower is better. |
| **Latency**  | Average seconds the model takes to translate one image. Lower is better (faster). |
| **Throughput** | How many images per second the model can process. Higher is better. |
---

## 4. Analysis of Parameter Impact (Finding the Sweet Spot)

- **BLEU vs. Params:** Plot translation quality against model size. You’ll usually see quality go up as models get bigger, but with smaller gains over time.  
- **Latency vs. Params:** Plot speed (time per image) against model size. Bigger models usually take longer.  
- **Trade‑off Surface:** Identify where you get most of the quality improvement without a big slowdown—that’s your “sweet spot.”
---

## 5. Next Steps (Putting It All Together)

1. **Get the Models**  
   - Ensure you have access (API endpoints or downloaded weights) for each model.

2. **Write Your Script**  
   - Automate the flow: load an image → preprocess → send to model → post‑process → record time + output.

3. **Run on Your Dataset**  
   - Use your chosen set of handwritten images (synthetic or real).

4. **Compute Metrics**  
   - Run BLEU, CHRF, TER scripts and log latency/throughput.

5. **Visualize & Decide**  
   - Create simple charts to compare quality vs. speed and choose the model that best fits your needs.

### Quick Glossary

- **Parameters:** “Brain size” of the model.  
- **Batch Size:** How many inputs you process at once.  
- **BLEU, CHRF, TER:** Automatic scores comparing AI text to human text.  
- **Latency & Throughput:** How fast the model works.

