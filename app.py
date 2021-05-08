import streamlit as st
from bokeh.models.widgets import Button
from bokeh.models import CustomJS

favicon = './favicon.png'
st.set_page_config(page_title='Text2Speech', page_icon = favicon, initial_sidebar_state = 'auto')
# favicon being an object of the same kind as the one you should provide st.image() with (ie. a PIL array for example) or a string (url or local file path)

hide_footer_style = """
    <style>
    .reportview-container .main footer {visibility: hidden;}    
    """
st.markdown(hide_footer_style, unsafe_allow_html=True)

st.write("""
## Clean and Simple Text to Speech WebApp
""")

text = st.text_input("Say what ?")

tts_button = Button(label="Speak", width=100)

tts_button.js_on_event("button_click", CustomJS(code=f"""
    var u = new SpeechSynthesisUtterance();
    u.text = "{text}";
    u.lang = 'en-US';

    speechSynthesis.speak(u);
    """))

st.bokeh_chart(tts_button)


st.write('\n')
st.write('\n')
st.write('\n')

st.write("""
#### Made with :heart: by Siddharth """)
# st.markdown(
#     """<a href="https://www.siddharthsah.com/">siddharthsah.com</a>""", unsafe_allow_html=True,
# )
link = '[siddharthsah.com](http://www.siddharthsah.com/)'
st.markdown(link, unsafe_allow_html=True)