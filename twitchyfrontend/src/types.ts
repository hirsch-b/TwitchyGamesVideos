export interface Game {
  twitch_id: string
  name: string
  box_art_url: string
}

export interface Video {
  twitch_id: string
  title: string
  description: string
  user_login: string
  user_name: string
  created_at: string
  published_at: string
  url: string
  thumbnail_url: string
  duration: string
  language: string
  view_count: number

  //   {
  //     "id": "",
  //     "stream_id": "",
  //     "user_id": "",
  //     "user_login": "",
  //     "user_name": "",
  //     "title": "",
  //     "description": "",
  //     "created_at": "2025-04-07T20:48:11+00:00",
  //     "published_at": "2025-04-07T20:48:11+00:00",
  //     "url": "",
  //     "thumbnail_url": "",
  //     "viewable": "public",
  //     "view_count": 0,
  //     "language": "pt",
  //     "type": "archive",
  //     "duration": "1h9m37s",
  //     "muted_segments": null
  // }
}
