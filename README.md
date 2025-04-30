# Cinefly_Backend_internship

## Summary of Steps

- **Rewrote core functions** – Ensured correct syntax for Python and Lambda compatibility.
- **Learned basic Lambda setup** – Reviewed AWS documentation for creating Python-based Lambda functions.
- **Watched testing tutorials** – Learned how to use test events in the Lambda console.
- **Performed basic validation** – Verified that input parameters and return values match expectations.


## Search Function Test Results

- All tests were performed using mock data and Lambda test events.

### Created a separate file for the mock back-end data


 ![Snap of the lambda handler in lambda IDE](Public/lambda_handler.png)

 ![Mock Data](Public/sample_data.png)

1. **Search Script Test Event**
   ![Search Script Test Event](Public/search_script_te.png)

    **Search Script Event Inputs**
   ![Search Script Event Inputs](Public/search_script_event_inputs.png)

    **Search Script TE Results**
   ![Search Script TE Results](Public/search_script_test_results.png)

2. **Search Listing Test Event**
   ![Search Listing Test Event](Public/search_listing_te.png)

    **Search Listing Event Inputs**
   ![Search Listing Event Inputs](Public/search_listing_event_inputs.png)

    **Search Listing TE Results**
   ![Search Listing TE Results](Public/search_listing_test_results.png)

3. **Search User Test Event**
   ![Search User Test Event](Public/search_user_te.png)

    **Search User Event Inputs**
   ![Search User Event Inputs](Public/search_user_event_inputs.png)

    **Search User TE Results**
   ![Search User TE Results](Public/search_user_test_results.png)

4. **Search Asset Test Event**
   ![Search Asset Test Event](Public/search_asset_te.png)

    **Search Asset Event Inputs**
   ![Search Asset Event Inputs](Public/search_asset_event_inputs.png)

    **Search Asset TE Results**
   ![Search Asset TE Results](Public/search_asset_test_results.png)

5. **Search ReusableAsset Test Event**
   ![Search ReusableAsset Test Event](Public/search_reusable_te.png)

    **Search ReusableAsset Event Inputs**
   ![Search ReusableAsset Event Inputs](Public/search_reusable_event_inputs.png)

    **Search ReusableAsset TE Results**
   ![Search ReusableAsset TE Results](Public/search_reusable_test_results.png)


## Project Function Test Results


![Snap of the lambda handler in lambda IDE](Public/lambda_handler_project.png)

 ![Mock Data and Functions](Public/mock_data_and_functions.png)

1. **Project Test Event 1**
   ![Project Test Event 1](Public/project_te1.png)

    **Project Fetched Successfully**
   ![Project Fetched Successfully](Public/project_test_results_success.png)

2. **Project Test Event 2**
   ![Project Test Event 2](Public/project_te2.png)

    **Project 400 Error**
   ![Project 400 Error](Public/project_test_results_400.png)

3. **Project Test Event 3**
   ![Project Test Event 3](Public/project_te3.png)

    **Project 404 Error**
   ![Project 404 Error](Public/project_test_results_404.png)