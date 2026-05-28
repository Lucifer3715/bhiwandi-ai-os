import streamlit as st
import datetime

# Page configuration
st.set_page_config(page_title="Bhiwandi AI OS: Licensing Hub", layout="wide", initial_sidebar_state="expanded")

# Custom CSS for Industrial High-Tech Look & Locked Screens
st.markdown("""
<style>
    .main { background-color: #0b0e14; color: #ffffff; }
    .cctv-box {
        border: 2px solid #232733;
        border-radius: 8px;
        padding: 10px;
        background-color: #121620;
        margin-bottom: 5px;
        position: relative;
    }
    .ai-badge {
        position: absolute;
        top: 15px;
        left: 15px;
        background-color: #00ff66;
        color: #000000;
        padding: 2px 8px;
        font-weight: bold;
        font-size: 11px;
        border-radius: 4px;
        text-transform: uppercase;
        box-shadow: 0 0 10px #00ff66;
        z-index: 10;
    }
    .camera-title {
        font-size: 16px;
        font-weight: bold;
        color: #ecf0f1;
        margin-bottom: 8px;
        text-align: left;
        padding-left: 5px;
    }
    .alert-box {
        padding: 10px;
        border-radius: 6px;
        margin-top: 8px;
        font-size: 13px;
        font-weight: 500;
    }
    .alert-danger {
        background-color: rgba(255, 75, 75, 0.15);
        border: 1px solid #ff4b4b;
        color: #ff4b4b;
    }
    .alert-success {
        background-color: rgba(0, 255, 102, 0.1);
        border: 1px solid #00ff66;
        color: #00ff66;
    }
    .lock-screen {
        text-align: center;
        padding: 50px;
        background-color: #1a0f12;
        border: 3px solid #ff4b4b;
        border-radius: 12px;
        margin-top: 50px;
        box-shadow: 0 0 30px rgba(255, 75, 75, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# 🌐 CENTRAL CLOUD SUBSCRIPTION ENGINE (State Management)
if 'current_plan' not in st.session_state:
    st.session_state['current_plan'] = "1 Week Trial (Active)"
if 'system_locked' not in st.session_state:
    st.session_state['system_locked'] = False

# Hard Expiry Display Screen
if st.session_state['system_locked']:
    st.markdown(f"""
    <div class='lock-screen'>
        <h1 style='color: #ff4b4b; font-size: 50px;'>❌ BHIWANDI AI OS: NETWORK LOCKED</h1>
        <h3 style='color: #ffffff;'>🚨 RECHARGE REQURED / LICENSE EXPIRED</h3>
        <p style='font-size: 18px; color: #aaa; margin-top: 20px;'>
            CCTV Vendor or Client subscription validity has ended. Systems disabled locally.
        </p>
        <div style='background-color: #ff4b4b; color: black; padding: 15px; font-size: 22px; font-weight: bold; border-radius: 6px; display: inline-block; margin-top: 20px;'>
            📞 Contact Master Distributor IKRAM JAFRI for Server Recharge Activation
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

# 🔑 PASSWORD PROTECTION LAYER
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

if not st.session_state['authenticated']:
    st.title("🔒 Bhiwandi AI OS Security Hub")
    password = st.text_input("Enter Master Security Password:", type="password")
    if st.button("Verify Key"):
        if password == "bhiwandi@2026":
            st.session_state['authenticated'] = True
            st.rerun()
        else:
            st.error("Invalid Security Key!")
    st.stop()

# 🎛️ SECRET OWNER CONTROL PANEL (Sidebar)
with st.sidebar:
    st.title("🛡️ Admin Licensing Node")
    st.markdown("### CCTV WITH AI SURVEILLANCE")
    st.write("---")
    
    # 🕵️‍♂️ HIDDEN RECHARGE SELECTION FOR IKRAM
    st.markdown("### ⚡ Master Recharge Portal")
    plan_options = [
        "1 Week Trial (Active)", 
        "1 Month Commercial", 
        "3 Month Commercial", 
        "6 Month Commercial", 
        "1 Year Enterprise", 
        "2 Year Long-Term Block"
    ]
    
    # Ikram can select the recharge plan here
    selected_plan = st.selectbox("Select Active Subscription Plan:", plan_options, index=plan_options.index(st.session_state['current_plan']))
    
    if selected_plan != st.session_state['current_plan']:
        st.session_state['current_plan'] = selected_plan
        st.success(f"Recharge Updated to: {selected_plan}")
        time_delay = 1
    
    st.metric(label="🟢 Active Server Plan", value=st.session_state['current_plan'])
    
    st.write("---")
    view_mode = st.radio("Select View Mode:", ["📦 Complete Factory Grid (All Cameras)", "🔍 Single Camera Focus Room"])
    
    # 🚨 ANTI-THEFT KILL SWITCH FOR VENDORS
    st.write("---")
    st.markdown("⚠️ **Vendor/CCTV Company Lock:**")
    if st.button("🚨 SIMULATE INSTANT SUBSCRIPTION EXPIRY"):
        st.session_state['system_locked'] = True
        st.rerun()

# 🏢 MAIN SURVEILLANCE DASHBOARD ELEVATION
st.markdown("<h1 style='text-align: center; color: #00ff66;'>🏢 BHIWANDI AI OS: INDUSTRIAL INTELLIGENCE CORE</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #aaa;'>⚡ Real-time Safety, Labor, Machine Mesh | Connected Plan: <b>{st.session_state['current_plan']}</b></p>", unsafe_allow_html=True)
st.write("---")

# 📊 INDUSTRIAL SIMULATION DATA
cameras = [
    {
        "id": 1, 
        "name": "📹 Camera 01: Main Production Floor (Line A)", 
        "video": "https://www.w3schools.com/html/mov_bbb.mp4", 
        "workers": 8, "machine": "CNC Machine 01 & 02: RUNNING", "gangway": "CLEAR",
        "alerts": ["🚨 2 Workers detected WITHOUT HELMET!", "🚨 1 Worker detected WITHOUT SAFETY SHOES!"]
    },
    {
        "id": 2, 
        "name": "📹 Camera 02: Finished Goods Dispatch Yard & Loading Dock", 
        "video": "https://www.w3schools.com/html/movie.mp4", 
        "workers": 5, "machine": "Forklift 01: ACTIVE", "gangway": "CLEAR",
        "alerts": ["🚨 Worker near loading bay detected WITHOUT SAFETY GLOVES!"]
    },
    {
        "id": 3, 
        "name": "📹 Camera 03: Raw Material Warehouse Corridor", 
        "video": "https://www.w3schools.com/html/mov_bbb.mp4", 
        "workers": 3, "machine": "No Heavy Machinery In Area", "gangway": "❌ BLOCKED",
        "alerts": ["🚨 CRITICAL: Wooden Pallets left in the middle of Walking Corridor/Gangway!"]
    },
    {
        "id": 4, 
        "name": "📹 Camera 04: Packaging & Box Stacking Area", 
        "video": "https://www.w3schools.com/html/movie.mp4", 
        "workers": 12, "machine": "Automatic Taping Conveyor: RUNNING", "gangway": "CLEAR",
        "alerts": ["✅ Safety Protocol 100% Stable. All workers wearing complete PPE."]
    },
]

# 🎚️ VIEW LOGIC
if view_mode == "📦 Complete Factory Grid (All Cameras)":
    col1, col2 = st.columns(2)
    for i, cam in enumerate(cameras):
        target_col = col1 if i % 2 == 0 else col2
        with target_col:
            st.markdown(f"""
            <div class='cctv-box'>
                <div class='ai-badge'>🤖 AI LIVE SURVEILLANCE</div>
                <div class='camera-title'>{cam['name']}</div>
            </div>
            """, unsafe_allow_html=True)
            st.video(cam['video'], autoplay=True, muted=True, loop=True)
            
            m1, m2, m3 = st.columns(3)
            m1.metric("👷 Live Workers", f"{cam['workers']} Persons")
            m2.metric("⚙️ Machine Status", "ACTIVE" if "RUNNING" in cam['machine'] or "ACTIVE" in cam['machine'] else "IDLE")
            m3.metric("🚶 Gangway Path", cam['gangway'])
            
            for alert in cam['alerts']:
                if "🚨" in alert:
                    st.markdown(f"<div class='alert-box alert-danger'>{alert}</div>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<div class='alert-box alert-success'>{alert}</div>", unsafe_allow_html=True)
            st.write("---")
else:
    st.markdown("### 🔍 Single Camera Focus Room (Maximized Window)")
    selected_cam_name = st.selectbox("Choose Camera to Maximize:", [cam['name'] for cam in cameras])
    cam = next(c for c in cameras if c['name'] == selected_cam_name)
    
    st.markdown(f"""
    <div class='cctv-box' style='border: 3px solid #00ff66;'>
        <div class='ai-badge' style='font-size: 14px; padding: 4px 12px;'>🤖 AI SURVEILLANCE MAX ACTIVE</div>
        <h2 style='color: #00ff66; text-align: left; padding-left: 10px; margin:0;'>{cam['name']}</h2>
    </div>
    """, unsafe_allow_html=True)
    st.video(cam['video'], autoplay=True, muted=True, loop=True)
    
    m1, m2, m3 = st.columns(3)
    m1.metric(label="👷 Live Workers Frame", value=f"{cam['workers']} Persons")
    m2.metric(label="⚙️ Machinery Status", value=cam['machine'])
    m3.metric(label="🚶 Gangway Compliance", value=cam['gangway'])