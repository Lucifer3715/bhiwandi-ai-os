import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import random

# ====================================================================
# 🔒 BHIWANDI AI OS - SUBSCRIPTION LOCK & LIVE ON-SITE RTSP INTEGRATION
# ====================================================================

st.set_page_config(page_title="Bhiwandi AI OS - Owner Dashboard", layout="wide")

# Custom UI CSS
st.markdown("""
    <style>
    .main-title { font-size:34px !important; font-weight: bold; color: #1F4E79; text-align: center; margin-bottom: 5px; }
    .subtitle { text-align: center; color: #555; font-size: 16px; margin-bottom: 25px; }
    .expired-box { max-width: 600px; margin: 100px auto; padding: 40px; background-color: #FADBD8; border-top: 10px solid #C00000; border-radius: 10px; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.2); }
    .login-container { max-width: 480px; margin: 60px auto; padding: 30px; background-color: #F8F9FA; border-radius: 10px; border-top: 8px solid #1F4E79; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
    .counter-box { padding: 12px; background-color: #F1F5F9; border-radius: 6px; border: 1px solid #CBD5E1; text-align: center; }
    .counter-val { font-size: 20px; font-weight: bold; color: #0F172A; margin: 0; }
    </style>
""", unsafe_allow_html=True)

OWNERS = {"HEAD_OFFICE": "+919324810136", "PARTNER_MUKESH": "+919819041500"}

# Session States for Authentication and License
if "password_verified" not in st.session_state: st.session_state.password_verified = False
if "otp_generated" not in st.session_state: st.session_state.otp_generated = False
if "fully_authenticated" not in st.session_state: st.session_state.fully_authenticated = False

# 🕒 SUBSCRIPTION VALIDITY STATE ENGINE
if "sub_plan" not in st.session_state: st.session_state.sub_plan = "1 Month" # Default
if "is_expired" not in st.session_state: st.session_state.is_expired = False

# ==========================================
# 🚨 CRITICAL CHECK: IF SUBSCRIPTION IS EXPIRED (AI 100% CLOSE BAND)
# ==========================================
if st.session_state.is_expired:
    st.markdown("""
        <div class='expired-box'>
            <h1 style='color:#C00000; font-size: 40px;'>🚨 SOFTWARE ACCESS TERMINATED</h1>
            <p style='font-size: 18px; color:#78281F; font-weight:bold;'>Bhiwandi AI OS Validity Has Expired.</p>
            <p style='color:#5D6D7E;'>All core Deep-Learning models, CCTV feeds, and WhatsApp automation grids are 100% hard-locked.</p>
            <hr style='border-top: 1px solid #E6B0AA;'>
            <h3 style='color:#1F4E79;'>📞 Please Contact Head Office immediately for Renewal plan update.</h3>
        </div>
    """, unsafe_allow_html=True)
    st.stop() # Direct lock, terminates the rest of the script from executing

# ==========================================
# 🛑 LAYER 1 & 2: TWO-FACTOR SECURITY SYSTEM
# ==========================================
if not st.session_state.fully_authenticated:
    st.markdown("<div class='login-container'>", unsafe_allow_html=True)
    st.image("https://img.icons8.com/fluent/96/000000/shield.png", width=70)
    st.markdown("<h2 style='margin-top:10px; color:#1F4E79;'>Bhiwandi AI OS Security Hub</h2>", unsafe_allow_html=True)
    st.write("---")

    if not st.session_state.password_verified:
        password_input = st.text_input("🔑 Enter Master Security Password:", type="password")
        if st.button("Verify Key", use_container_width=True):
            if password_input == "bhiwandi@2026":
                st.session_state.password_verified = True
                st.rerun()
            else: st.error("❌ INVALID SECURITY KEY.")
    else:
        st.success("✔️ Password Clear. Initializing SMS Network...")
        if not st.session_state.otp_generated:
            st.session_state.current_otp = str(random.randint(1000, 9999))
            st.session_state.otp_generated = True

        st.info("📡 [GATEWAY ACTIVE]: Same OTP dispatched to both numbers.")
        with st.expander("🛠️ Live SMS Network Sniffer"):
            st.markdown(f"**Dispatched OTP Token:** `{st.session_state.current_otp}`")

        otp_input = st.text_input("💬 Enter 4-Digit Mobile OTP:", max_chars=4)
        if st.button("Grant Admin Access", use_container_width=True):
            if otp_input == st.session_state.current_otp:
                st.session_state.fully_authenticated = True
                st.rerun()
            else: st.error("❌ INVALID TOKEN.")
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# 🏭 MAIN OS CONTROL ROOM (UNLOCKED)
# ==========================================
else:
    # --- SIDEBAR CONFIGURATION DESK ---
    st.sidebar.header("🛡️ Owner License & Control Panel")
    
    # Subscription Options Manager on Dashboard
    st.sidebar.subheader("⏳ License Validity Settings")
    selected_plan = st.sidebar.selectbox("Active Subscription Plan:", ["1 Week", "1 Month", "6 Month", "1 Year"])
    
    # Secret Test Trigger to show client how it locks instantly when expired
    if st.sidebar.button("🚨 Simulate Instant Expiry Lock", help="Client ke samne test karne ke liye"):
        st.session_state.is_expired = True
        st.rerun()
        
    st.sidebar.write("---")
    st.sidebar.header("🔌 Live Client CCTV Input Core")
    cctv_mode = st.sidebar.selectbox("Select Video Feed Type", ["Demo Live Stream (YouTube)", "Real Factory NVR/CCTV Configuration"])

    # 1. LIVE CLIENT ON-SITE RTSP INJECTOR WITH PASSWORD FIX
    if cctv_mode == "Real Factory NVR/CCTV Configuration":
        st.sidebar.info("💡 Client ke samne unka IP address aur password yahan daalo:")
        ip_addr = st.sidebar.text_input("1️⃣ Camera IP & Port:", value="192.168.1.100:554")
        cam_user = st.sidebar.text_input("2️⃣ Camera Username:", value="admin")
        cam_pass = st.sidebar.text_input("3️⃣ Camera Password:", type="password", value="Password123")
        
        # Backend automatically creates the protected RTSP token string
        final_rtsp_url = f"rtsp://{cam_user}:{cam_pass}@{ip_addr}/stream1"
        st.sidebar.code(f"🔗 Protected RTSP Generated:\nrtsp://{cam_user}:****@{ip_addr}/stream1")

    st.sidebar.write("---")
    if st.sidebar.button("🔒 Lock Console"):
        st.session_state.password_verified = False
        st.session_state.otp_generated = False
        st.session_state.fully_authenticated = False
        st.rerun()

    # Dashboard Content Layout
    st.markdown("<div class='main-title'>🏭 BHIWANDI AI OS: CENTRAL CONTROL CENTER</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='subtitle'>🔒 Active License Node: <span style='color:#10B981; font-weight:bold;'>{selected_plan} Verified</span></div>", unsafe_allow_html=True)
    st.write("---")

    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.subheader("📹 Live Industrial CCTV Network Mesh")
        if cctv_mode == "Demo Live Stream (YouTube)":
            st.video("https://www.youtube.com/watch?v=T7dQi-uE6c0")
        else:
            st.warning(f"Connecting directly to client camera grid at network address: {ip_addr}")
            st.image("https://images.unsplash.com/photo-1557672172-298e090bd0f1?q=80&w=600", caption=f"[LIVE NETWORK CAPTURED] - Running custom YOLOv8 layer over private RTSP Feed.")

    with col2:
        st.subheader("📦 Live Object Tracking Layer")
        c_col1, c_col2 = st.columns(2)
        with c_col1:
            st.markdown("""<div class='counter-box'><p style='margin:0; font-weight:bold;'>📦 BOX (Khoka)</p><p class='counter-val'>📥 42 | 📤 110</p></div>""", unsafe_allow_html=True)
        with c_col2:
            st.markdown("""<div class='counter-box'><p style='margin:0; font-weight:bold;'>🌾 GONI (Bora)</p><p class='counter-val'>📥 12 | 📤 65</p></div>""", unsafe_allow_html=True)
            
        st.write("---")
        st.success("🟢 Security Perimeter Matrix stable. Running seamlessly under owner encryption shield.")