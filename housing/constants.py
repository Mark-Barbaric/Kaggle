SUBMISSION_VERSION = "v2"
MAX_CARDINALITY = 11
Y_COLUMN = 'SalePrice'
NUMERICAL_COLS = ['LotFrontage', 'LotArea', 'Fireplaces', 'YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'BsmtFinSF1', 'BsmtFinSF2',
                         '1stFlrSF', '2ndFlrSF', 'LowQualFinSF', 'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath',
                         'Fireplaces', 'GarageYrBlt', 'GarageCars', 'GarageArea', 'WoodDeckSF', 'TotalBsmtSF', 'BsmtUnfSF',
                         'OpenPorchSF', 'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea', 'MiscVal', 'MoSold', 'YrSold']
ORDINAL_COLS = ['LandSlope', 'OverallQual', 'OverallCond', 'ExterQual', 'ExterCond',
                'BsmtQual', 'BsmtCond', 'BsmtExposure',
                'BsmtFinType1', 'BsmtFinType2', 'HeatingQC', 'KitchenQual', 'FireplaceQu', 'GarageFinish', 'GarageQual', 'GarageCond',
                'PoolQC', 'Fence']