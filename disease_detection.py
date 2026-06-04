def predict_disease(age, sugar, bp):
    if sugar > 140 and bp > 130:
        return "High risk of Diabetes and Heart Disease"
    elif sugar > 110:
        return "Moderate risk. Please monitor regularly."
    else:
        return "Low risk. You seem healthy."
