import { useState } from "react";
import {
  generateItinerary,
  checkTaskStatus,
  GenerateItineraryPayload,
  ItineraryStatusResponse,
} from "../services/itinerary";

const ItineraryForm = () => {
  const [destination, setDestination] = useState("");
  const [arrival, setArrival] = useState("");
  const [departure, setDeparture] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [result, setResult] = useState<any>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setResult(null);

    if (!destination || !arrival || !departure) {
      setError("All fields are required.");
      return;
    }

    const payload: GenerateItineraryPayload = {
      destination,
      arrival,
      departure,
    };

    try {
      setLoading(true);
      const taskId = await generateItinerary(payload);
      pollStatus(taskId);
    } catch (err) {
      setError("Something went wrong while generating the itinerary.");
      console.error(err);
    }
  };

  const pollStatus = (taskId: string) => {
    const interval = setInterval(async () => {
      const status: ItineraryStatusResponse = await checkTaskStatus(taskId);

      if (status.status === "Success") {
        clearInterval(interval);
        setResult(status.result);
        setLoading(false);
      } else if (status.status === "Failure") {
        clearInterval(interval);
        setError("Task failed: " + (status.error || "Unknown error"));
        setLoading(false);
      }
    }, 2000);
  };

  return (
    <div className="flex items-start justify-center min-h-screen bg-gray-50 px-4 py-10">
      <div className="w-full max-w-2xl space-y-8">
        <form
          onSubmit={handleSubmit}
          className="bg-white p-6 rounded-xl shadow-md space-y-4"
        >
          <h2 className="text-2xl font-semibold text-gray-800">
            Plan Your Travel Itinerary
          </h2>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Destination
            </label>
            <input
              type="text"
              value={destination}
              onChange={(e) => setDestination(e.target.value)}
              className="w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="e.g., Tokyo"
              required
            />
          </div>

          <div className="grid grid-cols-2 gap-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Arrival Date
              </label>
              <input
                type="date"
                value={arrival}
                onChange={(e) => setArrival(e.target.value)}
                className="w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
                required
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Departure Date
              </label>
              <input
                type="date"
                value={departure}
                onChange={(e) => setDeparture(e.target.value)}
                className="w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
                required
              />
            </div>
          </div>

          {error && <p className="text-red-600 text-sm">{error}</p>}

          <button
            type="submit"
            disabled={loading}
            className="w-full bg-blue-600 text-white font-semibold py-2 px-4 rounded-md hover:bg-blue-700 transition disabled:opacity-50"
          >
            {loading ? "Generating Itinerary..." : "Generate Itinerary"}
          </button>
        </form>

        {result && (
          <div className="bg-white p-6 rounded-xl shadow space-y-4">
            <h3 className="text-xl font-semibold text-gray-800">
              {result.title}
            </h3>
            <p className="text-gray-600">{result.description}</p>
            <p className="text-gray-500 text-sm">
              {result.location} | {result.arrival} → {result.departure}
            </p>

            {result.itinerary?.map((option: any) => (
              <div key={option.name} className="mt-4 border-t pt-4">
                <h4 className="font-semibold text-gray-700">{option.name}</h4>
                {option.days.map((day: any) => (
                  <div key={day.day} className="mt-2">
                    <p className="font-medium">{day.day}</p>
                    <ul className="list-disc list-inside text-sm text-gray-700">
                      {day.activities.map((act: string, idx: number) => (
                        <li key={idx}>{act}</li>
                      ))}
                    </ul>
                  </div>
                ))}
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

export default ItineraryForm;
