export interface ProfileModel {
  displayName: string;
  username: string;
  bio: string;
  homeTown: string;
  events: [string];
  genres: {
    name: string;
    endorsedBy: number
  }[];
}
