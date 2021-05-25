from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import RobustScaler, OneHotEncoder
from TaxiFareModel.encoders import TimeFeaturesEncoder, DistanceTransformer


def get_pipeline():
    ## Preproc
    ### Time
    time_features = ['pickup_datetime']

    time_pipe = make_pipeline(
        TimeFeaturesEncoder(time_column='pickup_datetime'),
        OneHotEncoder(handle_unknown='ignore')
        )
    ### Dist
    distance_features = [
        'pickup_latitude',
        'pickup_longitude',
        'dropoff_latitude',
        'dropoff_longitude'
        ]

    dist_pipe = make_pipeline(
        DistanceTransformer(p=1), 
        RobustScaler()
    )

    ## Preproc bloc
    preproc_bloc = ColumnTransformer([
        ('time', time_pipe, time_features),
        ('distance', dist_pipe, distance_features)
    ])

    ## Workflow
    pipeline = Pipeline([
        ('preproc', preproc_bloc),
        ('regression', LinearRegression())
        ]) 
    return pipeline
