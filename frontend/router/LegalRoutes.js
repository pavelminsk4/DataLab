import LegalView from '@views/LegalView'
import PrivacyScreen from '@components/legal/PrivacyScreen'
import TermsOfUseScreen from '@components/legal/TermsOfUseScreen'

export default [
  {
    name: 'Legal',
    path: '/legal',
    component: LegalView,
    redirect: () => ({name: 'Privacy'}),
    children: [
      {
        name: 'Privacy',
        path: 'privacy',
        component: PrivacyScreen,
      },
      {
        name: 'Terms',
        path: 'terms-of-use',
        component: TermsOfUseScreen,
      },
    ],
  },
]
