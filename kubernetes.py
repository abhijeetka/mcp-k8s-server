#!/usr/bin/env python3

from typing import Any
import subprocess
import json
import os
from mcp.server.fastmcp import FastMCP


env = os.environ.copy()
env["KUBECONFIG"] = "/Users/akamble/.kube/eks-devops"

mcp = FastMCP("kubernetes")

@mcp.tool()
async def get_pods(namespace: str = "default") -> dict:
    """Get all pods in the specified namespace"""
    try:
        cmd = ["kubectl", "get", "pods", "-n", namespace, "-o", "json"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        return {"error": f"Failed to get pods: {str(e)}"}

@mcp.tool()
async def get_failing_pods(namespace: str = "default") -> dict:
    """Get all pods with issues in the specified namespace"""
    try:
        cmd = ["kubectl", "get", "pods", "-n", namespace, "--field-selector=status.phase!=Running", "-o", "json"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        return {"error": f"Failed to get pods: {str(e)}"}

@mcp.tool()
async def get_services(namespace: str = "default") -> dict:
    """Get all services in the specified namespace"""
    try:
        cmd = ["kubectl", "get", "services", "-n", namespace, "-o", "json"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        return {"error": f"Failed to get services: {str(e)}"}

@mcp.tool()
async def describe_pod(pod_name: str, namespace: str = "default") -> dict:
    """Describe a specific pod"""
    try:
        cmd = ["kubectl", "describe", "pod", pod_name, "-n", namespace]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return {"description": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"error": f"Failed to describe pod: {str(e)}"}


@mcp.tool()
async def get_namespaces() -> dict:
    """Get all namespaces in the cluster"""
    try:
        cmd = ["kubectl", "get", "namespaces", "-o", "json"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        return {"error": f"Failed to get namespaces: {str(e)}"}
    
@mcp.tool()
async def get_nodes() -> dict:
    """Get all nodes in the cluster"""
    try:
        cmd = ["kubectl", "get", "nodes", "-o", "json"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        return {"error": f"Failed to get nodes: {str(e)}"}
    
@mcp.tool()
async def get_deployments(namespace: str = "default") -> dict:
    """Get all deployments in the specified namespace"""
    try:
        cmd = ["kubectl", "get", "deployments", "-n", namespace, "-o", "json"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        return {"error": f"Failed to get nodes: {str(e)}"}

@mcp.tool()
async def get_jobs(namespace: str = "default") -> dict:
    """Get all jobs in the specified namespace"""
    try:
        cmd = ["kubectl", "get", "jobs", "-n", namespace, "-o", "json"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        return {"error": f"Failed to get jobs: {str(e)}"}


@mcp.tool()
async def get_cronjobs(namespace: str = "default") -> dict:
    """Get all cronjobs in the specified namespace"""
    try:
        cmd = ["kubectl", "get", "cronjobs", "-n", namespace, "-o", "json"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        return {"error": f"Failed to get cronjobs: {str(e)}"}

@mcp.tool()
async def get_statefulsets(namespace: str = "default") -> dict:
    """Get all statefulsets in the specified namespace"""
    try:
        cmd = ["kubectl", "get", "statefulsets", "-n", namespace, "-o", "json"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        return {"error": f"Failed to get statefulsets: {str(e)}"}
    


@mcp.tool()
async def get_daemonsets(namespace: str = "default") -> dict:
    """Get all daemonsets in the specified namespace"""
    try:
        cmd = ["kubectl", "get", "daemonsets", "-n", namespace, "-o", "json"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        return {"error": f"Failed to get daemonsets: {str(e)}"}


@mcp.tool()
async def expose_service(name: str, namespace: str = "default", type: str = "LoadBalancer", port: int = 80, target_port: int = 80) -> dict:
    """Expose a service to the outside world"""
    try:
        cmd = ["kubectl", "expose", "service", name, "-n", namespace, "--type", type, "--port", str(port), "--target-port", str(target_port)]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        return {"error": f"Failed to expose service: {str(e)}"}


@mcp.tool()
async def port_forward(name: str, namespace: str = "default", port: int = 80, target_port: int = 80) -> dict:
    """Port forward a service to the outside world"""
    try:
        cmd = ["kubectl", "port-forward", "service", name, "-n", namespace, str(port), str(target_port)]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        return {"error": f"Failed to port forward service: {str(e)}"}
    


@mcp.tool()
async def get_logs(name: str, namespace: str = "default", tail: int = 1000) -> dict:
    """Get the logs of a specific pod"""
    try:
        cmd = ["kubectl", "logs", name, "-n", namespace, "--tail", str(tail)]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return {"logs": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"error": f"Failed to get logs: {str(e)}"}


@mcp.tool()
async def get_events(namespace: str = "default") -> dict:
    """Get the events of a specific namespace"""
    try:
        cmd = ["kubectl", "get", "events", "-n", namespace, "-o", "json"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        return {"error": f"Failed to get events: {str(e)}"}

   
@mcp.tool()
async def get_nodes(namespace: str = "default") -> dict:
    """Get the nodes of a specific namespace"""
    try:
        cmd = ["kubectl", "get", "nodes", "-n", namespace, "-o", "json"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        return {"error": f"Failed to get nodes: {str(e)}"}

@mcp.tool()
async def create_deployment(name: str, image: str, namespace: str = "default", replicas: int = 1) -> dict:
    """Create a Kubernetes deployment with specified name, image, namespace and replicas"""
    try:
        # Apply the deployment
        cmd = ["kubectl", "create", "deploy", name, 
               "--replicas", str(replicas), 
               "--image", image,
               "-n", namespace]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        return {"message": f"Deployment {name} created successfully in namespace {namespace}", 
                "details": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"error": f"Failed to create deployment: {str(e)}"}

@mcp.tool()
async def get_current_context() -> dict:
    """Get the current Kubernetes context"""
    try:
        cmd = ["kubectl", "config", "current-context"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return {"current_context": result.stdout.strip()}
    except subprocess.CalledProcessError as e:
        return {"error": f"Failed to get current context: {str(e)}"}

@mcp.tool()
async def list_contexts() -> dict:
    """List all available Kubernetes contexts"""
    try:
        cmd = ["kubectl", "config", "get-contexts", "-o", "name"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        contexts = result.stdout.strip().split('\n')
        return {"contexts": contexts}
    except subprocess.CalledProcessError as e:
        return {"error": f"Failed to list contexts: {str(e)}"}


@mcp.tool()
async def use_context(context: str) -> dict:
    """Use a specific Kubernetes context"""
    try:
        cmd = ["kubectl", "config", "use-context", context]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return {"message": f"Switched to context: {context}", 
                "details": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"error": f"Failed to switch context: {str(e)}"}

@mcp.tool()
async def update_deployment(name: str, namespace: str = "default", replicas: int = None, image: str = None) -> dict:
    """Update a Kubernetes deployment with new replicas count and/or image
    
    Args:
        name: Name of the deployment to update
        namespace: Namespace of the deployment
        replicas: New number of replicas (optional)
        image: New container image (optional)
    """
    try:
        if replicas is None and image is None:
            return {"error": "Must specify either replicas or image to update"}
            
        updates = []
        if replicas is not None:
            cmd = ["kubectl", "scale", "deployment", name,
                  "--replicas", str(replicas),
                  "-n", namespace]
            result = subprocess.run(cmd, capture_output=True, text=True, check=True )
            updates.append(f"Scaled replicas to {replicas}")
            
        if image is not None:
            cmd = ["kubectl", "set", "image", f"deployment/{name}",
                  f"{name}={image}",
                  "-n", namespace]
            result = subprocess.run(cmd, capture_output=True, text=True, check=True )
            updates.append(f"Updated image to {image}")
            
        return {
            "message": f"Deployment {name} updated successfully in namespace {namespace}",
            "updates": updates,
            "details": result.stdout
        }
    except subprocess.CalledProcessError as e:
        return {"error": f"Failed to update deployment: {str(e)}"}

if __name__ == "__main__":
    try:
        import logging
        logging.basicConfig(level=logging.INFO)
        logging.info("Starting Kubernetes MCP server...")
        mcp.run(transport='stdio')
    except Exception as e:
        logging.error(f"Failed to start server: {str(e)}")
        raise
