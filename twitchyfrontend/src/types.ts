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
}
