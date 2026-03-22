# DECISIONS

## Field Types

I used integer for the id field because IDs are numeric identifiers.

The name and workout_type fields are strings because they store text values.

Duration_minutes and calories_burned are integers because they represent numerical values related to workouts.

## Validation Rules

I used min_length and max_length for text fields to avoid empty or extremely long values.

I used gt=0 for duration_minutes to make sure workouts cannot have zero or negative duration.

I used ge=0 for calories_burned so that calories cannot be negative.

The age field also has constraints to ensure realistic member ages.

## Async Endpoint

The GET /members endpoint uses asyncio.sleep(1) to simulate a delay similar to a real database request.

This demonstrates how asynchronous endpoints work in FastAPI.