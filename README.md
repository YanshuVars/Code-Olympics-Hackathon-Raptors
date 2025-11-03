Perfect ✅ — here’s a **complete, professional-grade README.md** for your **CurveIQ** project.
It’s written in a polished, GitHub-friendly format, highlights your **“plot intersection”** novelty feature, and fits well for hackathons or portfolio display.

You can copy-paste this directly into your repo’s `README.md`.

---

# 🧠 CurveIQ — Compact Curve Analyzer

### ⚡ *A powerful 200-line Python CLI tool for mathematical curve analysis.*

CurveIQ is a **lightweight mathematical analysis engine** built entirely in Python using **SymPy**, **NumPy**, and **Matplotlib** — designed to analyze, visualize, and debug any mathematical curve directly from the command line.

Despite being under **200 lines of code**, it performs symbolic calculus, detects asymptotes, checks continuity, finds intersections, and even plots interactive graphs — all without any external GUI.

---

## 🚀 Features

| Category                                 | Description                                                                                                                                                                                         |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **🧩 Expression Analysis**               | Input any symbolic expression (e.g., `x**3 - 3*x + 2`) and get instant details — type, derivative, integral, roots, and periodicity.                                                                |
| **🧮 Calculus Operations**               | Compute derivatives (`diff`), integrals (`int`), and symbolic roots (`roots`) using SymPy’s engine.                                                                                                 |
| **🔍 Continuity & Limits**               | Evaluate left-hand and right-hand limits (`lim <point>`) and check continuity (`cont <point>`).                                                                                                     |
| **📈 Smart Plotting**                    | Plot any mathematical curve easily using `plot [a b]`. Uses NumPy & Matplotlib for smooth rendering.                                                                                                |
| **🪄 Novel Feature — Plot Intersection** | Use `inter <other_function>` to plot *two curves simultaneously* and automatically compute and mark their intersection points — a unique analytical visualization rarely seen in compact CLI tools. |
| **🧭 Curve Debugger (`dbg`)**            | Deep analysis mode to detect domain exclusions, asymptotes, stationary points, increasing/decreasing intervals, inflection points, and symmetry (even/odd).                                         |
| **💡 Minimalistic Design**               | Entirely under 200 lines of readable, modular Python code. Built for speed, simplicity, and hackathon performance.                                                                                  |

---

## 🧰 Tech Stack

* **Language:** Python 3.8+
* **Libraries:**

  * [SymPy](https://www.sympy.org) – symbolic computation
  * [NumPy](https://numpy.org) – numerical evaluation
  * [Matplotlib](https://matplotlib.org) – function plotting

---

## 🖥️ Usage

### ▶️ Run the App

```bash
python curveiq.py
```

### 🧭 Commands

| Command      | Description                                               |
| ------------ | --------------------------------------------------------- |
| `expr <f>`   | Set the current expression (e.g., `expr x**2 + 3*x - 4`)  |
| `diff`       | Display derivative                                        |
| `int`        | Display integral                                          |
| `roots`      | Show roots                                                |
| `lim <p>`    | Compute LHL/RHL at point p                                |
| `cont <p>`   | Check continuity at point p                               |
| `per`        | Display function periodicity                              |
| `plot [a b]` | Plot curve in range [a, b]                                |
| `inter <g>`  | Plot intersection with another function (✨ Novel Feature) |
| `dbg`        | Run curve debugger (domain, asymptotes, symmetry, etc.)   |
| `quit`       | Exit program                                              |

---

## 💡 Example Workflow

```bash
>> expr x**3 - 3*x + 2
>> diff
>> roots
>> lim 1
>> cont 1
>> plot -5 5
>> inter x**2
>> dbg
```

**Output:**

* Symbolic derivative/integral
* Root values
* Plot window with intersections
* Debug info: domain issues, asymptotes, stationary points, etc.

---

## ✨ Key Highlights

* 🔹 Built under **strict constraints** — all variable names ≤3 chars and total ≤200 lines.
* 🔹 Fully functional **CLI-based analytical tool** (no GUI dependencies).
* 🔹 Designed for **hackathon-level efficiency** and code compactness.
* 🔹 Supports both **symbolic** and **numeric** fallback methods for robust solving.
* 🔹 Novel *“Plot Intersection”* feature provides visual + analytical insight simultaneously.

---

## 🧠 Example — Plot Intersection

### Command

```bash
>> expr x**2 - 4
>> inter 2*x - 3
```

### Output

* Both functions plotted together.
* Intersection points automatically computed and highlighted in red.
* Printed coordinate pairs shown in console for reference.

*(A simple but powerful visual demonstration of analytical geometry.)*

---

## 🧩 Project Structure

```
CurveIQ/
│
├── curveiq.py     # Main CLI program (200 lines)
├── README.md       # Project documentation
└── requirements.txt # Dependencies (sympy, numpy, matplotlib)
```

---

## ⚙️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/curveiq.git
   cd curveiq
   ```
2. Install dependencies:

   ```bash
   pip install sympy numpy matplotlib
   ```
3. Run:

   ```bash
   python curveiq.py
   ```

---

## 🧩 Future Enhancements

* Add **3D curve plotting** (`plot3d` mode)
* Export results as **PDF reports**
* Add **automatic asymptote detection graph overlay**
* Support **parametric & polar functions**

---

## 🏅 Hackathon Context

> CurveIQ was built as part of a **Constraint-Based Coding Hackathon**,
> where each participant had to design a fully functional app within strict constraints:
>
> * Variable length ≤ 3 characters
> * Code length ≤ 200 lines

This constraint-driven creativity led to the birth of a **concise yet complete** mathematical analysis engine.

---

## 👩‍💻 Author

**Yanshu Varshney**
📍 Developer | Innovator | Hackathon Participant
💬 “Turning mathematical logic into interactive intelligence.”



# Code-Olympics-Hackathon-Raptors
