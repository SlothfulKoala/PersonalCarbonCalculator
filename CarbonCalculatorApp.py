import streamlit as st

EMISSION_FACTORS = {
    "India":{
        "Transportation":0.14, # kgCO2/km
        "Electricity":0.82, # kgCO2/KwH
        "Diet":1.25, #kgCO2/meal , 2.5 kgCO2/kg
        "Waste":0.12 #kgCo2/kg
    },

    "USA":{
        "Transportation":0.13, # kgCO2/km
        "Electricity":0.82, # kgCO2/KwH
        "Diet":1.25, #kgCO2/meal , 2.5 kgCO2/kg
        "Waste":0.12 #kgCo2/kg
    },

    "France":{
        "Transportation":0.09, # kgCO2/km
        "Electricity":0.82, # kgCO2/KwH
        "Diet":1.25, #kgCO2/meal , 2.5 kgCO2/kg
        "Waste":0.12 #kgCo2/kg
    }
}

st.set_page_config(layout="wide" , page_title="Personal Carbon Calculator")

st.title("Personal Carbon Calculator")

#user input
st.subheader("Your Country")
country=st.selectbox("Select",["India","USA","France"])

col1, col2 = st.columns(2)

with col1:
    st.subheader("Daily Commute Distance (in Km)")
    distance=st.slider("Distance",0.0,100.0,key="distance_input")

    st.subheader("Electricity Consumed in a month(in KwH)")
    electricity=st.slider("Electricity",0.0,1000.0,key="electricity_input")

    st.subheader("Number of Members in the Household")
    members=st.number_input("Members",1,key="member_input")

with col2:
    st.subheader("Waste Generated in a Week (in Kg)")
    waste=st.slider("Waste",0.0,100.0,key="waste_input")

    st.subheader("Meals eaten in a Day")
    meals=st.number_input("Meals",0,key="meals_input") 

# Normalizing the inputs
if distance>0:
    distance= distance*365 # convert the daily distance to yearly distance

if electricity>0:
    electricity = electricity / members
    electricity = electricity*12 # convert the monthly electricity consumption to yearly electricity consumption

if meals>0:
    meals = meals*365 # convert the meals per day to meals per year

if waste>0:
    waste = waste*52 # convert the weakly waste produced to yearly waste produced

# calculate the carbon emissions
transportation_emission = EMISSION_FACTORS[country]["Transportation"]*distance

electricity_emission = EMISSION_FACTORS[country]["Electricity"]*electricity

diet_emission = EMISSION_FACTORS[country]["Diet"]*meals

waste_emission = EMISSION_FACTORS[country]["Waste"]*waste

# conversion to tonnes and round off to 2 decimal places
transportation_emission=round(transportation_emission/1000,2)
waste_emission=round(waste_emission/1000,2)
diet_emission=round(diet_emission/1000,2)
electricity_emission=round(electricity_emission/1000,2)

# final result
total_emissions=round(transportation_emission+ waste_emission + electricity_emission + diet_emission,2)

if st.button("Calculate CO2 Emission"):

    # Displaying the Result
    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Carbon Emission by Categories:")
        st.info(f"Transpotation: {transportation_emission} tonnes CO2 per year")
        st.info(f"Electricity: {electricity_emission} tonnes CO2 per year")
        st.info(f"Waste: {waste_emission} tonnes CO2 per year")
        st.info(f"Diet: {diet_emission} tonnes CO2 per year")

    with col4:
        st.subheader("Total Carbon Footprint")
        st.info(f"Your Total Carbon Footprint is: {total_emissions} tonnes of CO2 per year")

        st.warning("Per capita carbon dioxide (CO₂) emissions in India have soared in recent decades,climbing from roughly 0.4 metric tons in 1970 to a high of 2.07 metric tons in 2023. This was an increase of 6.7 percent in comparison to 2022 levels.\nSource:https://www.iea.org/reports/co2-emissions-in-2023/energy-intensive-economic-growth-compounded-by-unfavourable-weather-pushed-emissions-up-in-china-and-india")

    