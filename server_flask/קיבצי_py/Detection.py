def Detect(frame, target_class):
    # הרצת המודל על התמונה
    results = model(frame)
    
    # המרת תוצאות ל-DataFrame
    df = results.pandas().xyxy[0]
    print(df)
    # סינון לפי המחלקה המבוקשת (class) ושמירה של התיבה עם ההסתברות הגבוהה ביותר
    filtered_df = df[df['class'] == target_class]
    
    # בדיקה אם אין תוצאות למחלקה המבוקשת
    if filtered_df.empty:
        print(f"לא נמצאו תוצאות עבור מחלקה {target_class}")
        return None

    # מציאת התיבה עם ההסתברות הגבוהה ביותר (העמודה 'confidence')
    best_row = filtered_df.loc[filtered_df['confidence'].idxmax()]

    # חישוב רוחב וגובה
    xmin, ymin, xmax, ymax = best_row['xmin'], best_row['ymin'], best_row['xmax'], best_row['ymax']
    width = xmax - xmin
    height = ymax - ymin
    
    print(f"התיבה התוחמת למחלקה {target_class} עם ההסתברות הגבוהה ביותר:")
    print(f"רוחב = {width}, גובה = {height}, הסתברות = {best_row['confidence']}")

    return height