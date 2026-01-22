"""Data loading utilities for fraud detection."""

import pandas as pd
import numpy as np
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def generate_fraud_data(n_samples: int = 10000, fraud_ratio: float = 0.1, save_path: Path = None) -> pd.DataFrame:
    """
    Generate synthetic fraud detection dataset.
    
    Args:
        n_samples: Total number of transactions to generate
        fraud_ratio: Proportion of fraudulent transactions
        save_path: Optional path to save the raw data
        
    Returns:
        DataFrame containing the fraud detection dataset
    """
    logger.info(f"Generating synthetic fraud detection dataset with {n_samples} samples...")
    
    np.random.seed(42)
    
    # Number of fraudulent transactions
    n_fraud = int(n_samples * fraud_ratio)
    n_legitimate = n_samples - n_fraud
    
    # Generate legitimate transactions
    legitimate_data = {
        'amount': np.random.exponential(scale=50, size=n_legitimate),
        'time_of_day': np.random.normal(loc=12, scale=4, size=n_legitimate),
        'transaction_frequency': np.random.poisson(lam=3, size=n_legitimate),
        'account_age_days': np.random.gamma(shape=2, scale=180, size=n_legitimate),
        'merchant_category': np.random.choice(['retail', 'online', 'grocery', 'gas'], size=n_legitimate),
        'distance_from_home': np.random.exponential(scale=10, size=n_legitimate),
        'previous_fraud_rate': np.random.beta(a=1, b=50, size=n_legitimate),
        'is_fraud': 0
    }
    
    # Generate fraudulent transactions (different patterns)
    fraudulent_data = {
        'amount': np.random.exponential(scale=200, size=n_fraud),  # Higher amounts
        'time_of_day': np.random.choice([0, 1, 2, 3, 23], size=n_fraud),  # Unusual times
        'transaction_frequency': np.random.poisson(lam=8, size=n_fraud),  # More frequent
        'account_age_days': np.random.gamma(shape=1, scale=30, size=n_fraud),  # Newer accounts
        'merchant_category': np.random.choice(['online', 'international'], size=n_fraud),
        'distance_from_home': np.random.exponential(scale=100, size=n_fraud),  # Far from home
        'previous_fraud_rate': np.random.beta(a=5, b=10, size=n_fraud),  # Higher fraud history
        'is_fraud': 1
    }
    
    # Combine data
    df_legitimate = pd.DataFrame(legitimate_data)
    df_fraudulent = pd.DataFrame(fraudulent_data)
    df = pd.concat([df_legitimate, df_fraudulent], ignore_index=True)
    
    # Shuffle the dataset
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    
    # Add transaction ID
    df.insert(0, 'transaction_id', range(1, len(df) + 1))
    
    logger.info(f"Generated dataset with shape: {df.shape}")
    logger.info(f"Fraud cases: {df['is_fraud'].sum()} ({df['is_fraud'].mean()*100:.2f}%)")
    logger.info(f"Legitimate cases: {(df['is_fraud']==0).sum()} ({(df['is_fraud']==0).mean()*100:.2f}%)")
    
    # Save raw data if path provided
    if save_path:
        save_path.mkdir(parents=True, exist_ok=True)
        file_path = save_path / "fraud_transactions.csv"
        df.to_csv(file_path, index=False)
        logger.info(f"Saved raw data to {file_path}")
    
    return df


def load_data_from_csv(file_path: Path) -> pd.DataFrame:
    """
    Load data from a CSV file.
    
    Args:
        file_path: Path to the CSV file
        
    Returns:
        DataFrame containing the data
    """
    logger.info(f"Loading data from {file_path}...")
    df = pd.read_csv(file_path)
    logger.info(f"Loaded dataset with shape: {df.shape}")
    
    if 'is_fraud' in df.columns:
        logger.info(f"Fraud cases: {df['is_fraud'].sum()} ({df['is_fraud'].mean()*100:.2f}%)")
    
    return df
