import pickle
upf = open('../data/model.pkl', 'rb')
mlr = pickle.load(upf, encoding='bytes') 
print(mlr)
# The coefficient and intercept
intercept = mlr.intercept_
coef = mlr.coef_

print('Intercept:', intercept)
print ('Coefficients:', coef)

#Create points predictor helper function
def predict_player_points(w, b, name):
    stats = players_dict[name]
    stats = list(stats) 
    estimate = round(np.dot(w, stats) + b)
    if estimate < 0:
        estimate = 0
    return estimate