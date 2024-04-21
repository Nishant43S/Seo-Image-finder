######  Librarys
import streamlit as st
import pandas as pd
import time
import random
from duckduckgo_search import DDGS
import requests
from PIL import Image
from io import BytesIO
import os

if __name__=="__main__":
    DEFAULT_DOWNLOAD_PATH = "downloads"

    def download_image(url,imageId):
        try:
            # Send a GET request to the URL
            response = requests.get(url)
            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Open the image using PIL
                image = Image.open(BytesIO(response.content))
                # Display the image
                
                # Download the image when the button is clicked
                if st.download_button(label="Download Image",
                                    data=response.content, 
                                    file_name="downloaded_image.jpg",key=f"{imageId}",
                                        mime="image/jpeg"):
                    if not os.path.exists(DEFAULT_DOWNLOAD_PATH):
                        os.makedirs(DEFAULT_DOWNLOAD_PATH)
                    filename = url.split("/")[-1]
                    download_path = os.path.join(DEFAULT_DOWNLOAD_PATH, filename)
                    with open(download_path, 'wb') as f:
                        f.write(response.content)
                    st.success(f"Image downloaded successfully! Download path: {download_path}")
            else:
                st.error(f"Failed to download image. Status code: {response.status_code}")
        except Exception as e:
            st.error(f"Failed to download image. Error: {e}")

   



st.set_page_config(
    page_title="Seo Image Finder",
    page_icon="📸",
    layout="centered",
    initial_sidebar_state="collapsed"
)   


Sidebar = st.sidebar

with Sidebar:
    st.header("Image Finder")
    st.subheader("Created By: Nishant Maity")
    st.write("---")
    st.subheader("Social Links")
    st.markdown(
        """
        <span style="margin-left: 26px;">
            <a href="https://www.linkedin.com/in/nishantmaity">
                <img src="https://th.bing.com/th/id/R.937670164b35c25a4d0c0c61dcfad542?rik=Evoppw8%2fFWa7fA&riu=http%3a%2f%2fpngimg.com%2fuploads%2flinkedIn%2flinkedIn_PNG17.png&ehk=H%2bEoCNPP4wNSh8TUxnbeOPk%2fOqo5pEjESYuV4OMahFU%3d&risl=&pid=ImgRaw&r=0" alt="Linked in" height="40" >
            </a>
        </span>
        
        <span style="margin-left: 26px;">
            <a href="https://github.com/Nishant43S">
                <img src="https://www.freeiconspng.com/thumbs/github-logo-icon/github-logo-icon-0.png" height="45" alt="github">
            </a>
        </span>
        
        <span style="margin-left: 26px;">
            <a href="https://www.instagram.com/invites/contact/?i=1ffha2jqxfo42&utm_content=m95jbmo">
                <img src="https://psfonttk.com/wp-content/uploads/2020/09/Instagram-Logo-Transparent-1024x987.png" height="40" alt="Instagram">
            </a>
        </span>
        """,unsafe_allow_html=True
    )


st.markdown(
    """
 <h1 style="color: orangered; cursor: pointer; transition: 0.3s ease-in;"
  >Seo Image Finder</h1>
""",
unsafe_allow_html=True
)
st.markdown(
    """
Seo Friendly image finder download images , gif , wallpaper. [Github](https://github.com/Nishant43S/Seo-Image-finder.git) Try app
"""
)
#### input fields
InputForm = st.form(key="Search Area",border=False)


with InputForm:
    Search_Quary = st.text_input(
        label="Search",type="default",
    )
    Result_col , ColourCol = st.columns([7,4])
    with Result_col:
        Number_Result = st.slider(
            label="Results",
            min_value=1,
            value=10,
            max_value=250,
            step=1
        )
    
    with ColourCol:
        ColourSceam = st.selectbox(
            label="Colour",
            options=[None,"color", "Monochrome", "Red", 'Orange', "Yellow", "Green", "Blue",
            'Purple', 'Pink', 'Brown', 'Black', 'Gray', 'Teal', "White"],
            index=0
        )

    ImgSize , ImgType , ImgLayout = st.columns(3)

    with ImgSize:
        ImageSize = st.selectbox(
            label="Image Size",
            options=[None,"Small", "Medium", "Large", "Wallpaper"],
            index=0
        )

    with ImgType:
        ImageType = st.selectbox(
            label="Image Type",
            options=["photo", "clipart", "gif", "transparent", "line"],
            index=0
        )
    with ImgLayout:
        ImageLayout = st.selectbox(
            label="Image Layout",
            options=[None,"Square", "Tall", "Wide"],
            index=0
        )
    c1 , c2 = st.columns([3,6])
    with c1:
        Search_Btn = st.form_submit_button(  ## Generate Button
            label="Generate",use_container_width=True
        )

    with c2:
        st.write(Search_Quary)

if Search_Btn:
    if Search_Quary.strip() == "":
        st.info("Enter prompt")
    else:
        if not  Search_Quary:
            st.stop()
        else:
            if __name__=="__main__":
                try:
                    Image_Results =  DDGS().images(   ### main finction 
                        keywords= Search_Quary,
                        region= "wt-wt",
                        safesearch= "off",
                        timelimit= None,
                        size = ImageSize,
                        color = ColourSceam,
                        type_image = ImageType,
                        layout = ImageLayout,
                        license_image= None,
                        max_results = Number_Result
                    )
                    dataF = pd.DataFrame(Image_Results)
                    Image_Links = []
                  
                    with st.spinner("Generating..."):
                        time.sleep(2)
                    for i in dataF["image"]:
                        Image_Links.append(i)
                    
                    Image_col1 , Image_col2 = st.columns(2)

                    with Image_col1:
                        if __name__=="__main__":
                            LeftRow = Image_Links[0::2]
                            random.shuffle(LeftRow)
                            for i in LeftRow:
                                try:
                                    st.image(i)
                                    downloadCo1 ,Linkcol1 = st.columns(2)
                                    with downloadCo1:
                                        if __name__ == "__main__":

                                            image_url = i
                                            if image_url:
                                                download_image(image_url,i)
                                    with Linkcol1:
                                        st.link_button(
                                            label="Image Link",
                                            url=i
                                        )
                                except:
                                    st.info("Something went wrong")
                    with Image_col2:
                        if __name__=="__main__":
                            RightRow = Image_Links[1::2]
                            random.shuffle(RightRow)
                            for j in RightRow:
                                try:
                                    st.image(j)
                                    downloadCo2 ,Linkcol2 = st.columns(2)
                                    with downloadCo2:
                                        if __name__ == "__main__":
                                            image_url = f"{j}"
                                            if image_url:
                                                download_image(image_url,j)
                                    with Linkcol2:
                                        st.link_button(
                                            label="Image Link",
                                            url=j
                                        )
                                except:
                                    st.info("Something went wrong")
                except Exception as err:
                    st.error(err)
                    st.info("Try after some time...")