import pickle
from scipy.sparse.sputils import get_sum_dtype
import streamlit as st
import math
import numpy as np

def haversine(lat1, lon1, lat2, lon2):
    R=6371000                               # radius of Earth in meters
    phi_1=math.radians(lat1)
    phi_2=math.radians(lat2)

    delta_phi=math.radians(lat2-lat1)
    delta_lambda=math.radians(lon2-lon1)

    a=math.sin(delta_phi/2.0)**2+\
        math.cos(phi_1)*math.cos(phi_2)*\
        math.sin(delta_lambda/2.0)**2
    c=2*math.atan2(math.sqrt(a),math.sqrt(1-a))
        
    meters=R*c                    # output distance in meters
    km=meters/1000.0              # output distance in kilometers
    miles=meters*0.000621371      # output distance in miles
    feet=miles*5280               # output distance in feet

    return miles
        
def predict(dist, hav, phr, dhr, temp, gtemp):

    input = np.array([dist, hav, phr, dhr, temp, gtemp])
    input = input.reshape(1,-1)
    
    duration = model.predict(input)

    return duration[0]

if __name__ == "__main__":
    st.title("Seoul Bike Trip Duration Prediction")
    #input = []
    st.markdown("Enter the distance travelled")
    dist = st.number_input("Distance")
    #input.append(dist)
    st.markdown("Enter the Latitude of coordinate1")
    lat1 = st.number_input("Latitude 1", format="%.5f")
    st.markdown("Enter the Longitude of coordinate1")
    lon1 = st.number_input("Longitude 1", format="%.5f")
    st.markdown("Enter the Latitude of coordinate1")
    lat2 = st.number_input("Latitude 2", format="%.5f")
    st.markdown("Enter the Longitude of coordinate2")
    lon2 = st.number_input("Longitude 2", format="%.5f")
    hav = haversine(lat1, lon1, lat2, lon2)
    st.markdown('Haversine: '+ str(np.round(hav, 2))+ ' miles')
    #input.append(hav)
    st.markdown("Enter the pickup hour")
    phr = st.slider("Pickup hour", min_value = 0, max_value = 23, value = 2, step = 1)
    #input.append(phr)
    st.markdown("Enter the drop hour")
    dhr = st.slider("Drop hour", min_value = 0, max_value = 23, value = 2, step = 1)
    #input.append(dhr)
    st.markdown("Enter the Temperature")
    temp = st.number_input("Temperature")
    #input.append(temp)
    st.markdown("Enter the Ground Temperature")
    gtemp = st.number_input("Ground Temperature")
    #input.append(gtemp)

    model = pickle.load(open('finalized_model.sav', 'rb'))

    #input = np.array([dist, hav, phr, dhr, temp, gtemp])
    #input = input.reshape(-1,1)

    if st.button("Predict"):
        dur = predict(dist, hav, phr, dhr, temp, gtemp)
        st.success("The predicted Duration: "+ str(np.round(dur, 2)) + ' miles')