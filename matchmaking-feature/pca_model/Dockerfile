FROM tensorflow/serving

COPY ./ /models/

CMD ["tensorflow_model_server", "--rest_api_port=8080", "--model_name=pca_model", "--model_base_path=/models/"]