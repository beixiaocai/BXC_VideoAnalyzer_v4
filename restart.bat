@echo off
taskkill /IM VideoAnalyzer.exe /F
taskkill /IM Admin.exe /F
taskkill /IM Analyzer.exe /F
taskkill /IM MediaServer.exe /F
taskkill /IM MediaManager.exe /F

VideoAnalyzer.exe
