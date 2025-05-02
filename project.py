# This is a placeholder for the backend logic.  A fully functional
# application would require a more complex setup with Django,
# database connections, and API endpoints.  This example focuses
# on demonstrating the core ML components and data flow.

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error  # Removed as it is not accessed
# import joblib  # Removed as it is not accessed
import datetime

# --- 1. Rainfall Prediction (Simplified) ---
def predict_rainfall(historical_rainfall_data, future_days=7):
    """
    Simplistic rainfall prediction using a linear regression model.
    In a real application, this would use a more sophisticated model
    and integrate with a weather API.

    Args:
        historical_rainfall_data (pd.Series): Historical rainfall data.
        future_days (int): Number of days to predict.

    Returns:
        pd.Series: Predicted rainfall for the next 'future_days'.
    """
    # Create a simple time series feature
    X = np.arange(len(historical_rainfall_data)).reshape(-1, 1)
    y = historical_rainfall_data.values

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions for the future
    future_X = np.arange(len(historical_rainfall_data), len(historical_rainfall_data) + future_days).reshape(-1, 1)
    predictions = model.predict(future_X)

    # Create a Pandas Series for the predictions
    future_dates = [datetime.date.today() + datetime.timedelta(days=i) for i in range(future_days)]
    predicted_rainfall = pd.Series(predictions, index=future_dates)

    return predicted_rainfall


# --- 2. Water Usage Forecasting (Simplified) ---
def forecast_water_usage(historical_usage_data, future_days=7):
    """
    Simplistic water usage forecasting using a linear regression model.
    In a real application, this would use a more sophisticated model
    and consider various factors.

    Args:
        historical_usage_data (pd.Series): Historical water usage data.
        future_days (int): Number of days to predict.

    Returns:
        pd.Series: Predicted water usage for the next 'future_days'.
    """
    # Create a simple time series feature
    X = np.arange(len(historical_usage_data)).reshape(-1, 1)
    y = historical_usage_data.values

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions for the future
    future_X = np.arange(len(historical_usage_data), len(historical_usage_data) + future_days).reshape(-1, 1)
    predictions = model.predict(future_X)

    # Create a Pandas Series for the predictions
    future_dates = [datetime.date.today() + datetime.timedelta(days=i) for i in range(future_days)]
    predicted_usage = pd.Series(predictions, index=future_dates)

    return predicted_usage


# --- 3. Leak Detection System (Simplified) ---
def detect_leak(recent_water_levels, threshold=0.1):
    """
    Detects leaks by checking for significant drops in water level.

    Args:
        recent_water_levels (list): List of recent water levels.
        threshold (float): Threshold for detecting a leak (percentage drop).

    Returns:
        bool: True if a leak is detected, False otherwise.
    """
    if len(recent_water_levels) < 2:
        return False  # Not enough data

    level_change = recent_water_levels[-1] - recent_water_levels[-2]
    percentage_change = level_change / recent_water_levels[-2]

    if percentage_change < -threshold:
        return True  # Leak detected
    else:
        return False  # No leak detected


# --- 4. Smart Water Allocation (Simplified) ---
def allocate_water(total_water_available, predicted_rainfall, predicted_usage, priorities={"drinking": 0.4, "cleaning": 0.3, "gardening": 0.3}):
    """
    Allocates water based on priorities and predictions.

    Args:
        total_water_available (float): Total water available in the tank.
        predicted_rainfall (pd.Series): Predicted rainfall for the next few days.
        predicted_usage (pd.Series): Predicted water usage for the next few days.
        priorities (dict): Dictionary of water usage priorities.

    Returns:
        dict: Water allocation for each need.
    """
    # Adjust priorities based on rainfall prediction
    if predicted_rainfall.mean() > 5:  # Example: If rainfall is high
        priorities["gardening"] = 0.4  # Increase gardening allocation
        priorities["drinking"] = 0.3  # Decrease drinking allocation (assuming less reliance on tank)
        priorities["cleaning"] = 0.3
    else:
        priorities["drinking"] = 0.4
        priorities["cleaning"] = 0.3
        priorities["gardening"] = 0.3

    # Calculate allocation based on priorities
    allocation = {}
    for need, priority in priorities.items():
        allocation[need] = total_water_available * priority

    # Adjust allocation based on predicted usage
    for need, amount in allocation.items():
        if need in predicted_usage.index:
            # Example: Reduce allocation if predicted usage is low
            if predicted_usage[need] < amount * 0.8:
                allocation[need] = predicted_usage[need] * 1.2  # Allocate slightly more than predicted

    return allocation


# --- 5. Water Storage Estimator (Simplified) ---
def estimate_water_storage(roof_area, rainfall_intensity, tank_capacity):
    """
    Estimates the amount of water that can be harvested.

    Args:
        roof_area (float): Roof area in square meters.
        rainfall_intensity (float): Rainfall intensity in mm/hour.
        tank_capacity (float): Tank capacity in liters.

    Returns:
        float: Estimated water that can be harvested in liters.
    """
    # Calculate the volume of water collected
    water_collected = roof_area * (rainfall_intensity / 1000)  # Convert mm to meters

    # Convert cubic meters to liters
    water_collected_liters = water_collected * 1000

    # Ensure the amount does not exceed tank capacity
    return min(water_collected_liters, tank_capacity)


# --- Example Usage ---
if __name__ == "__main__":
    # Sample data (replace with actual data from your system)
    historical_rainfall = pd.Series([1, 2, 0, 3, 1, 0, 2, 1, 0, 0], index=pd.date_range(start='2024-01-01', periods=10))
    historical_usage = pd.Series([10, 12, 8, 15, 11, 9, 13, 10, 7, 6], index=pd.date_range(start='2024-01-01', periods=10))
    recent_water_levels = [1000, 990, 980, 970, 960, 950, 940, 930, 920, 800]  # Example with a leak

    # 1. Rainfall Prediction
    predicted_rainfall = predict_rainfall(historical_rainfall)
    print("Predicted Rainfall:\n", predicted_rainfall)

    # 2. Water Usage Forecasting
    predicted_usage = forecast_water_usage(historical_usage)
    print("\nPredicted Water Usage:\n", predicted_usage)

    # 3. Leak Detection
    leak_detected = detect_leak(recent_water_levels)
    if leak_detected:
        print("\nLeak Detected!")
    else:
        print("\nNo Leak Detected.")

    # 4. Smart Water Allocation
    total_water_available = 1000  # Liters
    allocation = allocate_water(total_water_available, predicted_rainfall, predicted_usage)
    print("\nWater Allocation:\n", allocation)

    # 5. Water Storage Estimation
    roof_area = 100  # Square meters
    rainfall_intensity = 10  # mm/hour
    tank_capacity = 2000  # Liters
    estimated_storage = estimate_water_storage(roof_area, rainfall_intensity, tank_capacity)
    print("\nEstimated Water Storage:", estimated_storage, "liters")
