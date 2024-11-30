pipeline {
  agent { dockerfile true }
      
  stages {
         stage('Get Code') {
            steps {
                 git 'https://github.com/Averanc3/auto_qa_selenium_basics.git'
            }
         }
    stage('test') {
      steps {
        sh 'home/venv/bin/python -m pytest -v'
      }
      
      post {
        always {
          junit 'test-reports/*.xml'
        }
      }
    }
  }
}


