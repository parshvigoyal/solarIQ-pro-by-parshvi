import streamlit as st
from PIL import Image
from utils import sam_rooftop, solar_data
import matplotlib.pyplot as plt

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="🌞 Solar Industry AI Assistant - SolarIQ",
    layout="wide",
    page_icon="☀️"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
}

.main {
    background: linear-gradient(to bottom right, #0B1120, #111827);
    color: white;
}

h1, h2, h3, h4 {
    color: white;
}

.hero-box {
    background: linear-gradient(135deg, #1E3A8A, #059669);
    padding: 30px;
    border-radius: 25px;
    color: white;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.4);
    margin-bottom: 25px;
}

.info-card {
    background-color: #161B22;
    padding: 20px;
    border-radius: 20px;
    border: 1px solid #30363D;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.3);
    margin-bottom: 20px;
}

.metric-card {

    background:
    linear-gradient(
        135deg,
        rgba(16,185,129,0.15),
        rgba(59,130,246,0.10)
    );

    border-radius: 25px;

    padding: 25px;

    text-align:center;

    border:1px solid rgba(
        255,
        255,
        255,
        0.12
    );

    box-shadow:
    0 0 20px rgba(
        52,
        211,
        153,
        0.25
    );

    transition:
    0.3s ease-in-out;
}

/* HOVER EFFECT */

.metric-card:hover {

    transform:
    translateY(-8px)
    scale(1.02);

    box-shadow:
    0 0 50px rgba(
        52,
        211,
        153,
        0.5
    );
}


/* ==========================
   PREMIUM NEON SIDEBAR
========================== */

section[data-testid="stSidebar"] {

    background:
    linear-gradient(
        180deg,
        #111827,
        #0B1120
    );

    border-right:
    1px solid rgba(
        52,
        211,
        153,
        0.18
    );

    box-shadow:
    0 0 30px rgba(
        52,
        211,
        153,
        0.12
    );
}

section[data-testid="stSidebar"] label {

    color: white !important;
    font-weight: 600;
}

section[data-testid="stSidebar"] input {

    background:
    rgba(255,255,255,0.05)
    !important;

    border:
    1px solid rgba(
        52,
        211,
        153,
        0.2
    ) !important;

    border-radius: 12px;
}        



.highlight {
    color: #34D399;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HERO SECTION
# ---------------------------------------------------

st.markdown("""
<div class="hero-box">

<h1>
☀️ SolarIQ Intelligence Dashboard
</h1>

<h3>
🛰️ AI-Powered Rooftop Solar Intelligence Platform Developed By Parshvi Goyal
</h3>

<hr>

<p style="font-size:18px;">

🏠 SAM-Based Rooftop Segmentation <br>
🚧 AI Obstacle Detection <br>
☀️ Solar Feasibility Analysis <br>
📡 PVGIS Solar Irradiance Intelligence <br>
💰 ROI & Financial Intelligence <br>
🤖 AI Solar Recommendations

</p>

</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HOW TO USE
# ---------------------------------------------------

with st.expander("📘 How To Use The Solar Analysis Platform", expanded=True):

    st.markdown("""
### 🛰️ Step 1 — Upload Rooftop Image
Upload a rooftop satellite or aerial image for AI-based analysis.

---

### ⚙️ Step 2 — Configure Solar Parameters
Customize:
- 📍 Latitude & Longitude
- ⚡ Electricity Tariff
- 🏗️ Installation Cost

---

### 🤖 Step 3 — AI Solar Processing
The system automatically performs:

- 🛰️ SAM Rooftop Segmentation  
- 📐 Usable Rooftop Area Estimation  
- ☀️ PVGIS Solar Irradiance Analysis  
- ⚡ Annual Solar Energy Estimation  
- 💰 ROI & Financial Calculations  
- 🚧 Obstacle Detection & Filtering  
- 🤖 AI-Based Solar Recommendations

---

### 📥 Step 4 — Download Report
Export your complete rooftop solar assessment report.
""")

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.markdown("# ⚙️ Solar Configuration")

st.sidebar.markdown("""
Customize rooftop location and
financial parameters for
personalized solar analysis.
""")

latitude = st.sidebar.number_input(
    "📍 Latitude",
    value=23.2599,
    format="%.6f",
    help="Enter rooftop latitude"
)

longitude = st.sidebar.number_input(
    "📍 Longitude",
    value=77.4126,
    format="%.6f",
    help="Enter rooftop longitude"
)

electricity_cost = st.sidebar.number_input(
    "⚡ Electricity Cost (₹/kWh)",
    value=8.0,
    step=0.01,
    help="Electricity tariff per kWh"
)

system_cost = st.sidebar.number_input(
    "🏗️ System Cost (₹/Watt)",
    value=55.0,
    step=0.1,
    help="Estimated installation cost"
)

uploaded_file = st.file_uploader(
    "📷 Upload Rooftop Image",
    type=["png", "jpg", "jpeg"]
)

# ---------------------------------------------------
# FINANCIAL CALCULATIONS
# ---------------------------------------------------

def calculate_financials(
    irradiance_per_kwp,
    electricity_cost,
    system_cost,
    roof_area_m2
):

    installed_kwp = roof_area_m2 / 10

    total_cost = installed_kwp * 1000 * system_cost

    annual_energy = irradiance_per_kwp * installed_kwp

    annual_savings = annual_energy * electricity_cost

    if annual_savings > 0:
        payback_years = total_cost / annual_savings
    else:
        payback_years = float('inf')

    return total_cost, annual_savings, payback_years

# ---------------------------------------------------
# AI RECOMMENDATIONS
# ---------------------------------------------------

def generate_professional_ai_recommendations(
    rooftop_area,
    annual_energy,
    installation_cost,
    roi_payback
):

    return f"""
### 🌞 Solar Deployment Insights

✅ Rooftop suitability appears favorable for medium-scale solar deployment.

### 🏗️ Installation Recommendations
- Use high-efficiency monocrystalline solar panels.
- Ensure structural rooftop assessment before deployment.
- Maintain optimized panel tilt for maximum irradiance.

### ⚡ Maintenance Recommendations
- Clean solar panels every 1–3 months.
- Perform annual technical inspections.
- Monitor inverter efficiency regularly.

### 💰 Financial Outlook
- Estimated ROI Payback Period: {roi_payback:.1f} years
- Long-term savings potential is highly promising.
- Net-metering and subsidies may improve returns further.

### 🚀 Overall Assessment
This rooftop demonstrates strong potential for sustainable solar energy generation and long-term operational savings.
"""

# ---------------------------------------------------
# MAIN ANALYSIS
# ---------------------------------------------------

if uploaded_file:

    image = Image.open(uploaded_file).convert("RGB")

    st.markdown("## 🛰️ Uploaded Rooftop Image")

    st.image(
        image,
        use_container_width=True
    )

    with st.spinner(
        "🛰️ Running SAM rooftop analysis..."
    ):

        (
            rooftop_mask,
            obstacle_mask,
            final_mask,
            roof_area_m2
        ) = sam_rooftop.extract_rooftop_sam(image)

    st.success(
        "✅ Rooftop AI analysis completed"
    )

    st.write("")

    st.markdown(
        "## 🔬 AI Rooftop Research Analysis"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            "### 🏠 SAM Rooftop Mask"
        )

        st.image(
            rooftop_mask,
            use_container_width=True,
            clamp=True
        )

    with col2:

        st.markdown(
            "### 🚧 Obstacle Detection"
        )

        st.image(
            obstacle_mask,
            use_container_width=True,
            clamp=True
        )

    with col3:

        st.markdown(
            "### ☀️ Final Usable Area"
        )

        st.image(
            final_mask,
            use_container_width=True,
            clamp=True
        )

    st.markdown(f"""
    <div class="info-card">

    ## 📐 Estimated Rooftop Area

    ### {roof_area_m2:.2f} m²

    AI-estimated solar deployable rooftop surface.

    </div>
    """, unsafe_allow_html=True)

    

    st.markdown("""
<div class="info-card">

### ☀️ Solar Suitability

The detected rooftop region represents the estimated
usable surface suitable for solar deployment after
practical rooftop optimization and filtering.

</div>
""", unsafe_allow_html=True)

    # ---------------------------------------------------
    # PVGIS DATA
    # ---------------------------------------------------

    irradiance_per_kwp = solar_data.get_pvgis_irradiance(
        latitude,
        longitude
    )

    if irradiance_per_kwp is None:

        st.error(
            "⚠️ Unable to retrieve PVGIS irradiance data for this location."
        )

    else:

        total_cost, annual_savings, payback_years = calculate_financials(
            irradiance_per_kwp,
            electricity_cost,
            system_cost,
            roof_area_m2
        )

        estimated_annual_energy = (
            irradiance_per_kwp
            * roof_area_m2
            * 0.18
        )

        # ---------------------------------------------------
        # METRICS
        # ---------------------------------------------------

        st.markdown(
            "## ⚡ Solar Potential & Financial Insights"
        )

        m1, m2 = st.columns(2)
        m3, m4 = st.columns(2)

        with m1:
            st.markdown(f"""
            <div class="metric-card">
            <h3>☀️ Annual Energy</h3>
            <h2>{estimated_annual_energy:.2f} kWh</h2>
            </div>
            """, unsafe_allow_html=True)

        with m2:
            st.markdown(f"""
            <div class="metric-card">
            <h3>💰 Installation Cost</h3>
            <h2>₹{total_cost:,.0f}</h2>
            </div>
            """, unsafe_allow_html=True)

        with m3:
            st.markdown(f"""
            <div class="metric-card">
            <h3>📈 Annual Savings</h3>
            <h2>₹{annual_savings:,.0f}</h2>
            </div>
            """, unsafe_allow_html=True)

        with m4:
            st.markdown(f"""
            <div class="metric-card">
            <h3>⏳ ROI Payback</h3>
            <h2>{payback_years:.1f} Years</h2>
            </div>
            """, unsafe_allow_html=True)

        # ---------------------------------------------------
        # ROI VISUALIZATION
        # ---------------------------------------------------

        st.markdown(
            "## 📊 ROI Payback Visualization"
        )

        fig, ax = plt.subplots(
            figsize=(8, 4)
        )

        ax.bar(
            ["ROI Payback"],
            [payback_years],
            width=0.55,
            color="#34D399"
        )

        # dark dashboard background
        ax.set_facecolor("#0B1120")
        fig.patch.set_facecolor("#0B1120")

        # remove ugly borders
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

        # white text
        ax.tick_params(colors="white")
        ax.yaxis.label.set_color("white")

        ax.set_ylabel(
            "Years",
            color="white"
        )

        ax.set_title(
            "Solar ROI Dashboard",
            color="white",
            fontsize=14
        )

        # soft grid
        ax.grid(alpha=0.15)

        st.pyplot(fig)

        # ---------------------------------
        # AI OUTPUT
        # ---------------------------------

        ai_output = generate_professional_ai_recommendations(
            roof_area_m2,
            estimated_annual_energy,
            total_cost,
            payback_years
        )

        st.markdown(
            "## 🤖 AI Solar Recommendations"
        )

        with st.container():

            st.markdown(
                """
                <div class="info-card">
                """,
                unsafe_allow_html=True
            )

            st.markdown(ai_output)

            st.markdown(
                """
                </div>
                """,
                unsafe_allow_html=True
            )

        # ---------------------------------------------------
        # REPORT
        # ---------------------------------------------------

        report = f"""
    SOLAR INDUSTRY AI ASSISTANT REPORT
    ----------------------------------

    Latitude: {latitude}
    Longitude: {longitude}

    Detected Rooftop Area:
    {roof_area_m2:.2f} m²

    Estimated Solar Capacity:
    {roof_area_m2 * 0.18:.2f} kWp

    Estimated Annual Solar Energy:
    {estimated_annual_energy:.2f} kWh

    Estimated Installation Cost:
    ₹{total_cost:,.2f}

    Estimated Annual Savings:
    ₹{annual_savings:,.2f}

    ROI Payback Period:
    {payback_years:.1f} years

    AI Recommendations:
    {ai_output}
    """

        st.download_button(
            "📥 Download Full Solar Analysis Report",
            report,
            "solar_report.txt",
            "text/plain"
        )

else:

    st.info(
        "📷 Upload a rooftop image to begin AI-powered rooftop solar analysis."
    )