# MissiG (Linear Layout): Interactive Visualization of Multivarite Datasets with Missing Values

The purpose of this visualisation project is to highlight the effectiveness of the novel technique, Missing Glyph for its linear layout by modifying the original design, incorporating interactivity features into the design and conducting usability test on 3 datasets with different number of variables. 

## 🚀 Description

**Motivation:** Development & researches on the visualization techniques/tools used for visualizing missing patterns on the dataset are lacking despite its critical importances for data analysis and supporting data pre-processing decisions (removal or data imputation). Therefore, Missing Glyph visualisation is one of the techniques developed as a better alternatives to techniques like parallel coordinates and heatmaps. However, because it is still a new design, I've decided to investigate more about its effectiveness and by limiting my scope towards its linear layout. 

**Features: -**

* **Novel Glyph Design:** Encodes missingness patterns (AM, JM, CM) into intuitive visual components.
  * Amount Missing (AM) refers to how many values are missing in a single variable. It is encoded by the blue bar as shown below. 
<p align="center">
  <img width="210" height="312" alt="image" src="https://github.com/user-attachments/assets/a28f786e-60a9-4d94-a668-7d8ead99e3fd" />
</p>

  * Joint Missingness (JM) describes situations where two or more variables tend to have missing values in the same records. It is encoded by the red bar (on the right of the variable's container) and the red arcs linked between variables.
 <p align="center">
   <img width="598" height="372" alt="image" src="https://github.com/user-attachments/assets/12e9b64c-a8b0-4970-8152-0df530b898a6" />
 </p>
 
  * Conditional Missingness (CM) focuses on the relationship between missing values in one variable and the recorded values in another. This type of pattern helps uncover why certain values might be missing, offering insights that can guide imputation or analysis strategies. This pattern is shown by the recorded values which are the red histograms (positioned on the left side of the container). From the image below, missing values in Hours Studied corresponds to lower recorded values in Previous Scores and Performance Index. 
 <p align="center">
  <img width="1184" height="325" alt="image" src="https://github.com/user-attachments/assets/a7fecb32-d746-4c9d-bc76-e30a2442814a" />
 </p>
 
* **Interactive Exploration:** Features zooming, panning, and dynamic tooltips to reduce cognitive load. Image below shows that a tooltip will appear when you hover over an element in the visualization. 
<p align="center">
  <img width="240" height="325" alt="image" src="https://github.com/user-attachments/assets/dc411d52-fc47-4845-93ec-af21866e1c7c" />
</p>

* **Scalability:** Tested on datasets ranging from 6 to 22 variables.


## 🛠️ Tech Stack
* **Figma:** Used for UI/UX prototyping and layout optimization.
* **D3.js:** Core library for data-driven document manipulation and SVG rendering.
* **JavaScript (ES6+):** Logic for data preprocessing and interaction handling.
* **HTML5/CSS3:** Responsive container for the visualization dashboard.

## 📊 Evaluation & Findings
To evaluate the effectiveness of the MissiG visualization, a semi-structured interview was conducted with three university students (User A, B, and C) possessing varying levels of data visualization experience. The participants were asked a series of questions to assess the tool’s interpretability and usability across three datasets of increasing dimensionality: Student Performance (Small), Sleep Health and Lifestyle (Medium), and Kamyr Digester (Large). 

**Key findings: -**

* Participants successfully identified AM patterns across all datasets. However, detection became difficult in the large dataset for features with minimal missingness (e.g. a single missing value) without using zoom or hover functions.
* JM was the most intuitive pattern. Participants relied heavily on red arcs to identify relationships, especially as dimensionality increased and red bar indicators became too thin to notice.
* CM was the most complex pattern to interpret. While clear in the small dataset, users struggled with the medium and large datasets due to visual scaling, overlapping conditions, and a lack of domain-specific knowledge.
* The interface was found to be highly functional, with participants effectively using zooming, panning, and the reset key ('r') to navigate high-dimensional data.
* Interactive tooltips were deemed essential for confirming observations and distinguishing between features with low vs. zero missingness.
* In high-dimensional views, the bold outlines of bar charts sometimes obscured subtle visual indicators.
* Participants noted that using red for histograms (recorded values) caused confusion, as red was strongly associated with missingness indicators (arcs and bars).
* High-frequency categorical variables were sometimes misinterpreted as numerical variables due to the bin arrangement.
 
## ✅ Participant Feedback & Suggestions

* Adopt a more diverse color scheme and avoid using red for non-missingness data to reduce confusion.
* Incorporate an on-screen legend to serve as a quick reference for visual encodings.
* Explore alternative layouts beyond the current linear design to better accommodate extremely high-dimensional datasets.

## 💡 Conclusion
While MissiG with a linear layout is effective at lower dimensions, its interpretability decreases as dataset dimensionality increases.

## 📡 Live Visualization & Project Dissertation
Click here to view the project: [Home Page](https://imranar02.github.io/missing-glyph-linear-viz/)

