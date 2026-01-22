"""Data preprocessing utilities for fraud detection."""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from pathlib import Path
import logging
import pickle

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def preprocess_data(
    df: pd.DataFrame,
    test_size: float = 0.2,
    random_state: int = 42,
    save_path: Path = None
) -> tuple:
    """
    Preprocess the fraud detection data: encode, split and scale.
    
    Args:
        df: Input DataFrame
        test_size: Proportion of test set
        random_state: Random seed
        save_path: Optional path to save processed data
        
    Returns:
        Tuple of (X_train, X_test, y_train, y_test, scaler, encoders)
    """
    logger.info("Starting data preprocessing...")
    
    # Separate features and target
    feature_columns = [col for col in df.columns if col not in ['is_fraud', 'transaction_id']]
    
    # Encode categorical variables
    encoders = {}
    df_processed = df.copy()
    
    categorical_cols = df_processed[feature_columns].select_dtypes(include=['object']).columns
    for col in categorical_cols:
        encoder = LabelEncoder()
        df_processed[col] = encoder.fit_transform(df_processed[col])
        encoders[col] = encoder
        logger.info(f"Encoded categorical column: {col}")
    
    X = df_processed[feature_columns].values
    y = df_processed['is_fraud'].values
    
    logger.info(f"Features shape: {X.shape}, Target shape: {y.shape}")
    logger.info(f"Class distribution - Legitimate: {(y==0).sum()}, Fraud: {(y==1).sum()}")
    
    # Split data with stratification (important for imbalanced data)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    
    logger.info(f"Train set size: {len(X_train)}, Test set size: {len(X_test)}")
    logger.info(f"Train fraud rate: {y_train.mean()*100:.2f}%")
    logger.info(f"Test fraud rate: {y_test.mean()*100:.2f}%")
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Save processed data if path provided
    if save_path:
        save_path.mkdir(parents=True, exist_ok=True)
        
        np.save(save_path / "X_train.npy", X_train_scaled)
        np.save(save_path / "X_test.npy", X_test_scaled)
        np.save(save_path / "y_train.npy", y_train)
        np.save(save_path / "y_test.npy", y_test)
        
        # Save scaler
        with open(save_path / "scaler.pkl", 'wb') as f:
            pickle.dump(scaler, f)
        
        # Save encoders
        with open(save_path / "encoders.pkl", 'wb') as f:
            pickle.dump(encoders, f)
        
        # Save feature names
        with open(save_path / "feature_names.pkl", 'wb') as f:
            pickle.dump(feature_columns, f)
        
        logger.info(f"Saved processed data to {save_path}")
    
    return X_train_scaled, X_test_scaled, y_train, y_test, scaler, encoders
