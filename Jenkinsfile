pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/rnjacky777/auto_framework_2025.git'
            }
        }

        stage('Start Android Emulator') {
            steps {
                sh '''
                docker pull budtmo/docker-android-x86-11.0
                docker run --privileged -d --name android-emulator -p 6080:6080 -p 4723:4723 budtmo/docker-android-x86-11.0
                '''
            }
        }

        stage('Wait for Emulator Ready') {
            steps {
                // 等一下 emulator 完全啟動，避免太快跑測試失敗
                sh 'sleep 60'
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                pip install -r requirements.txt
                pytest tests/
                '''
            }
        }

        stage('Stop Android Emulator') {
            steps {
                sh '''
                docker stop android-emulator
                docker rm android-emulator
                '''
            }
        }
    }
    
    post {
        always {
            echo '清理環境'
            sh 'docker rm -f android-emulator || true'
        }
    }
}
