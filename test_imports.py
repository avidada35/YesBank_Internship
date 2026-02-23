#!/usr/bin/env python3
"""
Test script to verify all required libraries for Yes Bank Stock Prediction project.
This script imports every library from requirements.txt and reports success/failure.
"""

def test_imports():
    """Test all imports and report results."""
    print("🚀 Testing Python Library Imports for Yes Bank Project")
    print("=" * 60)
    
    # List of all libraries to test (based on requirements.txt and notebooks)
    libraries = [
        # Core Data Processing
        ("pandas", "pd"),
        ("numpy", "np"),
        
        # Visualization Libraries  
        ("matplotlib.pyplot", "plt"),
        ("seaborn", "sns"),
        ("plotly.express", "px"),
        ("plotly.graph_objects", "go"), 
        ("plotly.subplots", None),
        ("missingno", "msno"),
        
        # Machine Learning & Preprocessing
        ("sklearn.model_selection", None),
        ("sklearn.preprocessing", None), 
        ("sklearn.metrics", None),
        ("sklearn.linear_model", None),
        ("sklearn.ensemble", None),
        ("sklearn.svm", None),
        ("sklearn.feature_selection", None),
        ("xgboost", "xgb"),
        ("lightgbm", "lgb"),
        ("catboost", None),
        
        # Statistical & Time Series
        ("scipy.stats", "stats"),
        ("statsmodels.api", "sm"),
        ("ta", None),  # Technical analysis
        
        # Model Explainability
        ("shap", None),
        ("lime", None),
        
        # Model Persistence & Utilities
        ("joblib", None),
        ("pickle", None),  # Built-in, but good to test
        
        # Jupyter & Interactive
        ("IPython", None),
        ("ipywidgets", None),
        
        # Hyperparameter Optimization
        ("optuna", None),
        
        # Data Handling
        ("openpyxl", None),
        ("dotenv", None),
    ]
    
    passed = []
    failed = []
    
    # Test each import
    for lib_name, alias in libraries:
        try:
            if alias:
                exec(f"import {lib_name} as {alias}")
            else:
                exec(f"import {lib_name}")
            print(f"✅ {lib_name} is working")
            passed.append(lib_name)
        except ImportError as e:
            print(f"❌ ERROR: {lib_name} failed - {e}")
            failed.append(lib_name)
        except Exception as e:
            print(f"⚠️  WARNING: {lib_name} imported with issue - {e}")
            passed.append(lib_name)
    
    # Summary  
    print("\n" + "=" * 60)
    print(f"📊 SUMMARY: {len(passed)} passed, {len(failed)} failed")
    
    if failed:
        print(f"\n❌ Failed imports: {', '.join(failed)}")
        print("💡 Run: pip install -r requirements.txt")
        return False
    else:
        print("\n🎉 All libraries imported successfully!")
        print("✨ Your environment is ready for Yes Bank stock prediction!")
        return True

if __name__ == "__main__":
    success = test_imports()
    exit(0 if success else 1)