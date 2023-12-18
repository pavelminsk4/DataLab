export const userInfo = {
  user_profile: {department: {id: 1}, platform_language: 'en'},
}

export default {
  loading: false,
  loadingWidgets: {
    loading: false,
    clippingWidget: false,
  },
  workspaces: [],
  translation: {},
  platformLanguage: 'ar',
  translatedText: {header: '', text: ''},
  flashMessages: [],
  flashMessagesCount: 0,
  inreractiveDataModal: {
    isShow: false,
    data: {},
  },
  searchData: {},
  additionalFilters: {},
  userInfo,

  //widgets
  widgets: {
    hasAnimation: true,
  },
}
