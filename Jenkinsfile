pipeline {
  agent any
    environment {
      PATH = "/root/.local/bin:${env.PATH}"
    }
  stages {
    // Используем Docker агенты вместо master агента
    stage('Preparation') {
      steps {
        sh """
          apt-get update
          apt-get install -y python3 python3-pip
          ln -s /usr/bin/python3 /usr/bin/python || echo "Existing symlink"
          curl -LsSf https://astral.sh/uv/install.sh | sh
          python --version
          uv sync
        """
      }
    }
    stage('Build and Test') {
      steps {
        sh """
          ls -la
          uv run python hello-world.py
          echo "The code is okay"
        """
      }
    }
    stage('Lint') {
      steps {
        sh "uv run flake8 . --exclude=.git,.venv --show-source --statistics"
      }
    }
  }
}
