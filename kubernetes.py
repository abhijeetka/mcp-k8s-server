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
async def expose_service(k8s_object: str, name: str, namespace: str = "default", type: str = "ClusterIP", port: int = 80, target_port: int = 80, protocol: str = "TCP") -> dict:
    """Expose a resource as a new kubernetes service
       k8s_object can be pod (po), service (svc), replicationcontroller (rc), deployment (deploy), replicaset (rs)
       Type for this service: ClusterIP, NodePort, LoadBalancer, or ExternalName. Default is 'ClusterIP'.
    """
    try:
        cmd = ["kubectl", "expose", k8s_object, name, "-n", namespace, "--type", type, "--port", str(port), "--target-port", str(target_port),"--protocol", protocol]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        return {"error": f"Failed to expose : {str(e)}"}


@mcp.tool()
async def port_forward(k8s_object: str, name: str, namespace: str = "default", port: int = 80, target_port: int = 80) -> dict:
    """Port forward a resource to the outside world
        k8s_object can be a pod, deployment or a service and it should be in the format pod/<name>, deployment/<name>, service/<name>
    """
    try:
        cmd = ["kubectl", "port-forward", k8s_object, name, "-n", namespace, str(port), str(target_port)]
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
async def use_context(context_name: str) -> dict:
    """Switch to a specific Kubernetes context
    Args:
        context_name: The name of the Kubernetes context to switch to
    """
    try:
        cmd = ["kubectl", "config", "use-context", context_name]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return {"message": f"Switched to context: {context_name}",
                "details": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"error": f"Failed to switch context: {str(e)}"}

@mcp.tool()
async def annotate_resource(resource_type: str, resource_name: str, annotation: str, namespace: str = "default") -> dict:
    """Annotate a Kubernetes resource with the specified annotation

    Args:
        resource_type: Type of the resource (e.g., pod, service, deployment)
        resource_name: Name of the resource to annotate
        annotation: Annotation to add (e.g., key=value)
        namespace: Namespace of the resource
    """
    try:
        cmd = ["kubectl", "annotate", resource_type, resource_name, annotation, "-n", namespace, "--overwrite"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return {"message": f"Resource {resource_type}/{resource_name} annotated successfully in namespace {namespace}",
                "details": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"error": f"Failed to annotate resource: {str(e)}"}


@mcp.tool()
async def remove_annotation(resource_type: str, resource_name: str, annotation_key: str, namespace: str = "default") -> dict:
    """Remove an annotation from a Kubernetes resource

    Args:
        resource_type: Type of the resource (e.g., pod, service, deployment)
        resource_name: Name of the resource to remove the annotation from
        annotation_key: Key of the annotation to remove
        namespace: Namespace of the resource
    """
    try:
        cmd = ["kubectl", "annotate", resource_type, resource_name, f"{annotation_key}-", "-n", namespace, "--overwrite"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return {"message": f"Annotation {annotation_key} removed from resource {resource_type}/{resource_name} in namespace {namespace}",
                "details": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"error": f"Failed to remove annotation: {str(e)}"}

@mcp.tool()
async def label_resource(resource_type: str, resource_name: str, label: str, namespace: str = "default") -> dict:
    """Label a Kubernetes resource with the specified label

    Args:
        resource_type: Type of the resource (e.g., pod, service, deployment)
        resource_name: Name of the resource to label
        label: Label to add (e.g., key=value)
        namespace: Namespace of the resource
    """
    try:
        cmd = ["kubectl", "label", resource_type, resource_name, label, "-n", namespace, "--overwrite"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return {"message": f"Resource {resource_type}/{resource_name} labeled successfully in namespace {namespace}",
                "details": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"error": f"Failed to label resource: {str(e)}"}

@mcp.tool()
async def remove_label(resource_type: str, resource_name: str, label_key: str, namespace: str = "default") -> dict:
    """Remove a label from a Kubernetes resource

    Args:
        resource_type: Type of the resource (e.g., pod, service, deployment)
        resource_name: Name of the resource to remove the label from
        label_key: Key of the label to remove
        namespace: Namespace of the resource
    """
    try:
        cmd = ["kubectl", "label", resource_type, resource_name, f"{label_key}-", "-n", namespace, "--overwrite"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return {"message": f"Label {label_key} removed from resource {resource_type}/{resource_name} in namespace {namespace}",
                "details": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"error": f"Failed to remove label: {str(e)}"}


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

@mcp.tool()
async def delete_resource(resource_type: str, resource_name: str, namespace: str = "default") -> dict:
    """Delete a Kubernetes resource

    Args:
        resource_type: Type of the resource (e.g., pod, service, deployment,configmap,secret,ingress,statefulset,replicaset,damonset,newtorkpolicy,rolebinding,role,serviceaccount,job,cronjob)
        resource_name: Name of the resource to delete
        namespace: Namespace of the resource
    """
    try:
        cmd = ["kubectl", "delete", resource_type, resource_name, "-n", namespace]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return {"message": f"Resource {resource_type}/{resource_name} deleted successfully in namespace {namespace}",
                "details": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"error": f"Failed to delete resource: {str(e)}"}


if __name__ == "__main__":
    try:
        import logging
        logging.basicConfig(level=logging.INFO)
        logging.info("Starting Kubernetes MCP server...")
        mcp.run(transport='stdio')
    except Exception as e:
        logging.error(f"Failed to start server: {str(e)}")
        raise
