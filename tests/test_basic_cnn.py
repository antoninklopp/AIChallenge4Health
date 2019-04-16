from src.models.basic_cnn import get_model

if __name__ == "__main__":
    model, x_test, y_test = get_model()
    model.evaluate(x_test, y_test)