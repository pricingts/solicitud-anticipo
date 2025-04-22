import streamlit as st
import pandas as pd
from services.auth import check_authentication

st.set_page_config(page_title="Solicitud de Anticipo", layout="wide")

def identity_role(email):
    admin = [
        "manager@tradingsolutions.com", "jsanchez@tradingsolutions.com", "pricing2@tradingsolutions.com", "pricing@tradingsolutions.com", "pricing@tradingsol.com",
        "manager@tradingsol.com", "jsanchez@tradingsol.com", "pricing2@tradingsol.com", "sjaafar@tradingsol.com"
    ]

    commercial = [
        "sales2@tradingsolutions.com", "sales1@tradingsolutions.com", "sales3@tradingsolutions.com", "sales4@tradingsolutions.com", "sales@tradingsolutions.com",
        "sales5@tradingsolutions.com", "bds@tradingsolutions.com", "insidesales@tradingsolutions.com", "sales6@tradingsolutions.com", "sales5@tradingsolutions.com"

        "sales2@tradingsol.com", "sales1@tradingsol.com", "sales3@tradingsol.com", "sales4@tradingsol.com", "sales@tradingsol.com",
        "sales5@tradingsol.com", "bds@tradingsol.com", "insidesales@tradingsol.com", "sales6@tradingsol.com", "sales5@tradingsol.com"
    ]

    inside =["pricing7@tradingsolutions.com", "traffic2@traingsolutions.com", "pricing7@tradingsol.com", "traffic2@traingsol.com"]

    if email in admin:
        return "admin"
    elif email in inside:
        return "inside"
    elif email in commercial:
        return "commercial"
    else:
        return None

@st.dialog("Warning", width="large")
def non_identiy():
    st.write("Dear user, it appears that you do not have an assigned role on the platform. This might restrict your access to certain features. Please contact the support team to have the appropriate role assigned. Thank you!")
    st.write("sjaafar@tradingsolutions.com")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image("resources/images/logo_trading.png", width=800)

check_authentication()
role = identity_role(st.experimental_user.email)

if role is None:
    non_identiy()
else:
    user = st.experimental_user.name

    if role in ["commercial", "admin", "inside"]:
        with st.sidebar:
            page = st.radio("Go to", ["Home",  "Generar Documento"])

        if page == "Generar Documento":
            import views.Payment_Request as payment 
            payment.show(role)
