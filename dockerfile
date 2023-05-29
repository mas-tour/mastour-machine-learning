FROM tensorflow/serving

COPY model/ /models/

CMD ["tensorflow_model_server", "--rest_api_port=8501", "--model_name=my_model", "--model_base_path=/models/"]
