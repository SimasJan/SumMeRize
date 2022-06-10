import streamlit as st
import warnings
import backend

if __name__ == "__main__":

    st.title("SumMeRize")

    # load entity options
    entities_filename = 'spacy_v3.3.1_entities.json'
    entity_options = backend.load_files(entities_filename, True)

    # read input
    source = st.text_input("Article URL", value="BBC.co.uk", help="Enter the URL an article")
    entities = st.multiselect("Entities", entity_options)

    print(entities, source)

    # make first request
    response = backend.make_request(source)
    soup = backend.make_soup(response)

    # find all tags whose name starts (^) and ends ($) with letter "p".
    target = "^p$"
    parsed_data = backend.parse_html(soup, target)
    text_str = parsed_data.get('string')

    doc = backend.make_spacy_document(text_str, model="en_core_web_sm")
    # print('DOC: ', doc)
    if doc:
        # find entities
        results = []
        for ent in entities:
            res = backend.find_entities(doc, ent, unique=False)
            st.write(str(res))
            # show = backend.print_template(ent, res)
            # st.write(show)