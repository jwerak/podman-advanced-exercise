package main

import (
	"fmt"
	"os"
	"os/signal"
	"syscall"
	"time"
)

var (
	shutdownSignals = []os.Signal{os.Interrupt, syscall.SIGTERM}
)

func main() {
	fmt.Println("Starting application - NEW")
	stopChannel := setupSignalHandler()

	fmt.Println("Waiting for receiving event to stop")

	<-stopChannel
	fmt.Println("Received stop signal, performing cleanup")
	performCleanup()
	fmt.Println("Cleanup finished, exiting")
}

func setupSignalHandler() (stopCh <-chan struct{}) {
	fmt.Println("Creating signal handler")

	stop := make(chan struct{})
	c := make(chan os.Signal, 1) // Buffer of 1 is enough
	signal.Notify(c, shutdownSignals...)
	go func() {
		<-c
		close(stop) // Notify main to start cleanup
	}()
	return stop
}

func performCleanup() {
	// Simulate cleanup within a reasonable time
	time.Sleep(1 * time.Second) // Ensure this is less than `podman stop`'s grace period
}