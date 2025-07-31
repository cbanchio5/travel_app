export interface GenerateItineraryPayload {
  destination: string;
  arrival: string;   // ISO format: 'YYYY-MM-DD'
  departure: string; // ISO format
}

export interface GenerateItineraryResponse {
  task_id: string;
}

export interface ItineraryStatusSuccess {
  status: 'Success';
  result: any; // You can define a specific ItineraryResult type if needed
}

export interface ItineraryStatusPending {
  status: 'Pending';
}

export interface ItineraryStatusFailure {
  status: 'Failure';
  error: string;
}

export type ItineraryStatusResponse =
  | ItineraryStatusSuccess
  | ItineraryStatusPending
  | ItineraryStatusFailure;

export async function generateItinerary(
  payload: GenerateItineraryPayload
): Promise<string> {
  const response = await fetch("http://localhost:8000/test-generator/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  const data: GenerateItineraryResponse = await response.json();

  if (!response.ok) {
    throw new Error("Failed to start itinerary task");
  }

  return data.task_id;
}

export async function checkTaskStatus(
  taskId: string
): Promise<ItineraryStatusResponse> {
  const response = await fetch(
    `http://localhost:8000/itinerary-status/${taskId}/`
  );
  const data: ItineraryStatusResponse = await response.json();
  return data;
}
