export interface ItineraryOption {
  title: string;
  description: string;
  location: string;
  arrival: string;
  departure: string;
  itinerary: {
    [optionKey: string]: {
      [dayKey: string]: string[];
    };
  };
}
