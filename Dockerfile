# Use a small Python base image
FROM python:3.12-slim

# Create a non-root user
RUN addgroup --system appgroup && adduser --system appuser --ingroup appgroup

# Set working directory
WORKDIR /home/appuser/app

# Copy the application code
COPY app/ .

# Install required Python packages
RUN pip install flask pytz

# Switch to non-root user
USER appuser

# Expose port
EXPOSE 8080

# Run the application
CMD ["python", "app.py"]

